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