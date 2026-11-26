import networkx as nx


def some(adj_list, red_vertices, s, t, directed):
    """True if s-t path contains a red vertex.
        Undirected: biconnected components   Directed: only DAGs 
        
        Arguments: 
        adj_list: adjacency dictionary, mapping each vertex to a list of its neighbors (list).
        red_vertices: set of red vertices, 
        s: start vertex, 
        t: end vertex, 
        directed: (bool)
        
        Returns:
            (bool) or "?!" if graph is directed and has a cycle
        """
    #build graphs with networkx
    G = nx.DiGraph() if directed else nx.Graph()
    G.add_nodes_from(adj_list)
    G.add_edges_from((u, v) for u in adj_list for v in adj_list[u] if u != v)


    # if directed, check if DAG  or not
    if directed:
        if not nx.is_directed_acyclic_graph(G):
            return "?!"
        # check everything reachable from s
        from_s = nx.descendants(G,s) | {s}
        # check everything that can reach t
        to_t = nx.ancestors(G,t) | {t}
        #returning any path from s to t that goes through a red vertex
        return any(r in from_s and r in to_t for r in red_vertices)

    # check first if s-t path is possible:
    if not nx.has_path(G, s, t):
        return False

    # add temporary edge between s-t, so everything is one block
    G.add_edge(s, t)
    for block in nx.biconnected_components(G):
        if s in block and t in block:
            # check if any red vertex is in the same block as s and t
            return any(r in block for r in red_vertices)

    return False
