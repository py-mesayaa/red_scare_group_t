from pathlib import Path
from build_graphs import parse_graph
from many import solve_many
from none import none
from few import few
from alternate import alternate
from some import some
import json

data_dir = Path("../red-scare/data")
files = sorted(data_dir.glob("*.txt"))

results = {}

for path in files:

    # Parse graph once
    adj_list, reds, s, t, directed = parse_graph(path)

    # Run algorithms
    alternate_answer = alternate(adj_list, reds, s, t)
    many_answer = solve_many(adj_list, reds, s, t, directed)
    none_answer = none(adj_list, reds, s, t)
    few_answer = few(adj_list, reds, s, t)
    some_answer = some(adj_list, reds, s, t, directed)

    results[path.stem] = {
        "n": len(adj_list),
        "A": alternate_answer,
        "F": few_answer,
        "M": many_answer,
        "N": none_answer,
        "S": some_answer
    }
    
# Create result directory if it doesn't exist
result_dir = Path("result")
result_dir.mkdir(parents=True, exist_ok=True)

# Save results
result_file = result_dir / "results.txt"

with result_file.open("w") as f:
    json.dump(results, f, indent=4)

print(f"Results saved to {result_file}")


# create LATEX table
def format_result(value):
    if value is None:
        return "--"
    return str(value)


def latex_escape(text):
    return str(text).replace("_", r"\_")


rows = []

for name, data in results.items():
    rows.append(
        f"{latex_escape(name)} & "
        f"{data['n']:,} & "
        f"{format_result(data['A'])} & "
        f"{format_result(data['F'])} & "
        f"{format_result(data['M'])} & "
        f"{format_result(data['N'])} & "
        f"{format_result(data['S'])} \\\\"
    )

table = r"""
\begin{table}[ht]
\centering
\begin{tabular}{l r c r r r r}
\hline
Instance name & $n$ & A & F & M & N & S \\
\hline
""" + "\n".join(rows) + r"""
\hline
\end{tabular}
\caption{Results for all graph instances.}
\label{tab:results}
\end{table}
"""

table_file = result_dir / "results_table.tex"

with table_file.open("w") as f:
    f.write(table)

print(f"Table saved to {table_file}")