from build_graphs import parse_graph
from pathlib import Path
from collections import deque
from collections import defaultdict, deque

def bfs_reachability(adj_list, s, t):
    if s == t:
        return True
    visited = set()
    visited.add(s)
    queue = deque([s])
    
    while queue:
        v = queue.popleft()
        neighbors = adj_list[v]
        if t in neighbors:
            return True
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def topological_order(adj_list):
    """
    Kahn's algorithm for topological sorting.

    Argument:
        adj_list: dict mapping vertex -> list of neighbours (as returned by parse_graph)

    Returns:
        list of vertices in topological order, or None if the graph contains a cycle.

    Running time: O(n + m).

    Based on Kahn (1962)
    """
    indeg = {v: 0 for v in adj_list}

    for u in adj_list:
        for v in adj_list[u]:
            indeg[v] += 1

    queue = deque(v for v in adj_list if indeg[v] == 0)

    order = []
    while queue:
        u = queue.popleft()
        order.append(u)

        for v in adj_list[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)

    if len(order) != len(adj_list):
        return None
    return order       

def many_dag(adj_list, reds, s, t, topo):
    """Max red vertices on an s->t path in a DAG. O(n + m)."""
    NEG = -10**15
    dist = {v: NEG for v in adj_list}
    dist[s] = 1 if s in reds else 0 

    for u in topo:
        if dist[u] == NEG:
            continue
        for v in adj_list[u]:
            cand = dist[u] + (1 if v in reds else 0)
            if cand > dist[v]:
                dist[v] = cand

    return -1 if dist[t] == NEG else dist[t]   




def many_one_red(adj_list, reds, s, t):
    """
    Undirected graph, exactly one red vertex w. Returns 1 if a simple
    s-t path passes through w, else 0. Vertex-split max-flow, need flow >= 2.
    Based on Menger's theorem
    """
    w = next(iter(reds))

    # Free special cases
    if s == t:
        return 1 if s in reds else 0
    if w == s or w == t:
        return 1

    IN, OUT = 0, 1
    cap = defaultdict(lambda: defaultdict(int))

    def add(u, v, c):
        cap[u][v] += c
        cap[v][u] += 0

    for v in adj_list:
        add((v, IN), (v, OUT), 1)
        for u in adj_list[v]:
            add((v, OUT), (u, IN), 1)

    source = (w, OUT)
    sink = ("__sink__",)
    add((s, OUT), sink, 1)
    add((t, OUT), sink, 1)

    def augment():
        """One BFS augmenting path; returns flow pushed (0 if none)."""
        parent = {source: None}
        q = deque([source])
        while q and sink not in parent:
            u = q.popleft()
            for v in cap[u]:
                if v not in parent and cap[u][v] > 0:
                    parent[v] = u
                    q.append(v)
        if sink not in parent:
            return 0
        path, v = [], sink
        while parent[v] is not None:
            u = parent[v]
            path.append((u, v))
            v = u
        pushed = min(cap[u][v] for u, v in path)
        for u, v in path:
            cap[u][v] -= pushed
            cap[v][u] += pushed
        return pushed

    flow = 0
    while flow < 2:
        p = augment()
        if p == 0:
            break
        flow += p
    return 1 if flow >= 2 else 0

def main():
    data_dir = Path("../red-scare/data")
    files = sorted(data_dir.glob("*.txt"))

    dag_directed    = []   # directed, reachable, acyclic
    dag_undirected  = []   # undirected, reachable, acyclic -> only possible if edgeless
    cyclic_directed = []   # directed, reachable, but cyclic
    ready_for_dp    = []   # (name, adj_list, reds, s, t, topo)

    results = {}

    for path in files:
        adj_list, reds, s, t, directed = parse_graph(path)

        # Step 1: reachability. Unreachable instances are already solved -> -1.
        if not bfs_reachability(adj_list, s, t):
            results[path.stem] = (-1, "unreachable")
            continue
        
        # Step 2: no red vertices. Already reachable, so answer is 0 (any path has zero reds)
        if len(reds) == 0:
            results[path.stem] = (0, "no_red")     
            continue

        # Step 3: undirected + exactly one red. flow solver
        if not directed and len(reds) == 1:
            results[path.stem] = (many_one_red(adj_list, reds, s, t), "one_red")
            continue

        # Step 4: Kahn's. Returns an order, or None if cyclic.
        topo = topological_order(adj_list)

        if topo is None:
            if directed:
                cyclic_directed.append(path.stem)
            continue

        if directed:
            dag_directed.append(path.stem)
        else:
            dag_undirected.append(path.stem)

        ready_for_dp.append((path.stem, adj_list, reds, s, t, topo))

    for name, adj_list, reds, s, t, topo in ready_for_dp:
        results[name] = (many_dag(adj_list, reds, s, t, topo), "dag")

    # the rest is not solvable by polynomial algorithms, hence we label them "?!"
    for path in files:
        name = path.stem
        if name not in results:
            results[name] = ("?!", "np_hard")
    return results

if __name__=="__main__":
    main()
