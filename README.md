# VCG Cheapest Path
## Description

The function `vcg_cheapest_path(graph, source, target)`:

1. Finds the cheapest path from **source** to **target** using NetworkX.
2. Calculates the VCG payment for each edge on that path:

   ```
   payment_e = cost(path without e) - (total_cost - cost(e))
   ```
3. Prints the chosen path, its total cost, and each edge’s payment (formatted as a float).

## Installation

```bash
pip install networkx
```

## Usage

```bash
python vcg_cheapest_path.py
```

## Example

```python
import networkx as nx
from vcg_cheapest_path import vcg_cheapest_path

# Build a sample graph
G = nx.DiGraph()
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=5)

# Compute VCG payments
vcg_cheapest_path(G, 'A', 'C')
```

**Expected output:**

```
Path chosen: ['A', 'B', 'C']
Total cost: 3
Payment for edge ('A', 'B'): 3.0
Payment for edge ('B', 'C'): 4.0
```

## Credits

chatGPT - [Link](https://chatgpt.com/share/68237c40-e690-800b-982f-3a81d2f2be7f)


