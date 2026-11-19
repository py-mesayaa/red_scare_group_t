
from collections import deque
from build_graphs import parse_graph
from pathlib import Path

def few(adj_list, red_vertices, s, t):
    distances = {}

    for vertex in adj_list:
        distances[vertex] = float("inf")

    if s in red_vertices:
        distances[s] = 1
    else:
        distances[s] = 0

    queue = deque ([s])

    while queue:
        current = queue.popleft()

        for neighbor in adj_list[current]:
            if neighbor in red_vertices:
                cost = 1
            else:
                cost = 0

            new_distance = distances[current] + cost

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

                if cost == 0:
                    queue.appendleft(neighbor)
                else:
                    queue.append(neighbor)

    if distances[t] == float("inf"):
        return -1
    else:
        return distances[t]


if __name__ == "__main__":
    data_folder = Path("red-scare/data")

    for path in sorted(data_folder.glob("*.txt")):
        adj_list, red_vertices, s, t, directed = parse_graph(path)
        result = few(adj_list, red_vertices, s, t)
        print(f"{path.name}: FEW = {result}")
