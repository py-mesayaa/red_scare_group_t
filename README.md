# Red Scare — Group T

Solutions for the **Red Scare!** graph algorithms exercise (MSc Algorithm Design). 

The project implements algorithms for the five problem variants: Alternate, Few, Many, None, and Some. The solutions are evaluated on all graph instances provided in the exercise dataset.

Official problem statement and instance gallery: [`red-scare/doc/red-scare.pdf`](red-scare/doc/red-scare.pdf). Report skeleton: [`red-scare/doc/report.pdf`](red-scare/doc/report.pdf).

## Repository layout

red_scare_group_t/
├── red-scare/
│   ├── data/                 # Graph instances
│   └── doc/                  # Problem statement and report template
├── src/
│   ├── create_results.py     # Main script for generating all results
│   ├── build_graphs.py       # Graph parsing and construction
│   ├── many.py               # MANY algorithm
│   ├── few.py                # FEW algorithm
│   ├── none.py               # NONE algorithm
│   ├── some.py               # SOME algorithm
│   └── alternate.py          # ALTERNATE algorithm
├── requirements.txt
├── README.md
└── ...

### Prerequisites

<!-- e.g. Python 3.11+, pip install -r requirements.txt -->

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