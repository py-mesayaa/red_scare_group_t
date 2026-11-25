from collections import deque
from build_graphs import parse_graph
from pathlib import Path

def none(adj_lst, red_vertices, s, t):
    normal_vertices = set()

    for vertex in adj_lst:
        if vertex not in red_vertices or vertex == s or vertex == t:
            normal_vertices.add(vertex)

    dists = {}
    dists[s] = 0
    queue = deque([s])

    while queue:
        current = queue.popleft()

        for neighbour in adj_lst[current]:
            if neighbour in normal_vertices and neighbour not in dists:
                dists[neighbour] = dists[current] + 1
                queue.append(neighbour)

    if t in dists:
        return dists[t]
    else:
        return -1

