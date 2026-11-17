from itu.algs4.graphs.graph import Graph
from itu.algs4.graphs.digraph import Digraph

def parse_graph(path):
    """ Read Red scare instance file into an adjacency list.

    Arguments:
        path: path to the .txt in red_scare/data
    
    Returns:
        adj_list: adjacency dictionary, mapping each vertex to a list of its neighbors (list).
                For undirected edges ("--"), the neighbor is added to both vertices' lists.
        reds: set of red vertices, 
        s: start vertex, 
        t: end vertex, 
        directed: (bool)
    """
    with open(path) as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    # n: number of nodes
    # m: number of edges
    # r: number of red vertices
        n, m, r = map(int, lines[0].split())
    # s: start vertex
    # t: end vertex
        s, t = lines[1].split()

        reds = set()
        adj_list = {}

        for line in lines[2:2+n]:
            parts = line.split()
            adj_list[parts[0]] = []
            if len(parts) > 1 and parts[1] == "*":
                reds.add(parts[0])

        directed = False
        for line in lines[2 + n:]:
                v, sym, u = line.split()
                adj_list[v].append(u)
                if sym == "--":
                    adj_list[u].append(v)
                else:
                    directed = True

        return adj_list , reds, s, t, directed


def to_algs4(adj_list, directed, keep_edge = lambda v, u: True):
    """ Convert adjacency list to an instance of Graph or Digraph from the itu.algs4, 
        so the BFS, dijskta and other algorithms can be used from the library."""
    names = list(adj_list)
    index = {name: i for i, name in enumerate(names)}
    G = Digraph(len(names)) if directed else Graph(len(names))
    for v in names:
        for u in adj_list[v]:
            if u == v or not keep_edge(v, u):
                #dropping self-loops as covered in the description
                continue
            if directed or index[v] < index[u]:
                G.add_edge(index[v], index[u])

    return G, index, names
