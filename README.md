# Red Scare — Group T

Solutions for the **Red Scare!** graph algorithms exercise (MSc Algorithm Design). 

The project implements algorithms for the five problem variants: Alternate, Few, Many, None, and Some. The solutions are evaluated on all graph instances provided in the exercise dataset.

Official problem statement and instance gallery: [`red-scare/doc/red-scare.pdf`](red-scare/doc/red-scare.pdf). Report skeleton: [`red-scare/doc/report.pdf`](red-scare/doc/report.pdf).


## Repository layout

```text
red_scare_group_t/
├── red-scare/
│   ├── data/                               # Graph instances
│   └── doc/
│       ├── red-scare.pdf                   # Official problem statement
│       └── Red_Scare_report___Group_T.pdf  # Final group report
│
├── src/
│   ├── build_graphs.py                     # Graph parsing and construction
│   ├── create_results.py                   # Runs all algorithms and generates results
│   ├── alternate.py                        # ALTERNATE solution
│   ├── few.py                              # FEW solution
│   ├── many.py                             # MANY solution
│   ├── none.py                             # NONE solution
│   ├── some.py                             # SOME solution
│   │
│   ├── results/
│   │   └── results.txt                     # Generated results for all instances
│   │
│   └── testing/                            # Tests and experimental scripts
│
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```


### Prerequisites

networkx, numpy, itu.algs4

### Installation and recreating results

git clone https://github.com/py-mesayaa/red_scare_group_t.git

cd red_scare_group_t

pip install -r requirements.txt

cd src

python create_results.py

## Deliverables

1. **Report** — follow [`red-scare/doc/report.pdf`](red-scare/doc/report.pdf)
2. **`results.txt`** — full result table for all instances in `red-scare/data/`.
3. **Programs and this README** — enough detail for someone to regenerate `results.txt` from scratch.


Originated from [thorehusfeldt/algdes-labs](https://github.com/thorehusfeldt/algdes-labs).