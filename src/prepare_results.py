from pathlib import Path
from build_graphs import parse_graph
from few import few

def all_results(algorithm):
    data_folder = Path("red-scare/data")
    results = []

    for path in sorted(data_folder.glob("*.txt")):
        adj_list, red_vertices, s, t, directed = parse_graph(path)
            
        n = len(adj_list)
        result = algorithm(adj_list, red_vertices, s, t)

        results.append((path.stem, n, result))
    return results

def report_500_plus(algorithm):
    results = all_results(algorithm)

    for name, n, result in results:
        if n >= 500:
            print(f"{name}: n = {n}, result = {result}")

if __name__ == "__main__":
    print("ALL RESULTS")
    for name, n, result in all_results(few):
        print(f"{name}: n = {n}, result = {result}")

    print("\nREPORT RESULTS (500+ VERTICES)")
    report_500_plus(few)