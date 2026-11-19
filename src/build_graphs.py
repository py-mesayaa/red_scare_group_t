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


def to_algs4(adj_list : dict, directed: bool, keep_edge = lambda v, u: True):
    """ Convert adjacency list to an instance of Graph or Digraph from the itu.algs4, 
        so the BFS, dijskta and other algorithms can be used from the library.
        
    Arguments:
        adj_list: (dict) adjacency dictionary from parse_graph
        directed: (bool) from parse_graph, True if graph is directed, else False
        keep_edge: (function) a function that takes two vertices v and u and returns True if the edge (v, u) should be kept, False otherwise. 
                    This can be used to filter out certain edges based on custom criteria.
    Returns:
        G: an instance of Graph or Digraph from itu.algs4 
        index: a dictionary mapping vertex names to their corresponding indices in the graph
        names: a list of vertex names in the order they were added to the graph.
        """

    names = list(adj_list)
    index = {name: i for i, name in enumerate(names)}
    G = Digraph(len(names)) if directed else Graph(len(names))
    for v in names:
        for u in adj_list[v]:
            if u == v or not keep_edge(v, u):
                #dropping self-loops as covered in the description
                continue
            if directed:
                # one direction edge as Digraph - just one way from v -> u
                G.add_edge(index[v], index[u])
            elif index[v] < index[u] and keep_edge(v, u) and keep_edge(u, v):
                # undirected edges
                # each undirected edge appears in both adjacency lists, but Graph.add_edge
                # links both ends, so only add the copy where index[v] < index[u]
                G.add_edge(index[v], index[u])    

    return G, index, names
