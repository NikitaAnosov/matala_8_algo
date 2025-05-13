import networkx as nx

def vcg_cheapest_path(graph, source, target):
    """
    Finds the cheapest path from source to target using NetworkX,
    then computes a VCG payment for each edge in that path.

    VCG payment for edge e:
        p_e = cost(P_without_e) - (cost(P_with_e) - cost(e))

    where:
      - cost(P_with_e) is the total cost of the chosen path P*
      - cost(P_without_e) is the total cost of the cheapest path
        when edge e is removed from the graph
      - cost(e) is the weight of edge e in the chosen path

    Prints each edge and its payment.

    >>> G = nx.DiGraph()
    >>> G.add_edge('A', 'B', weight=1)
    >>> G.add_edge('B', 'C', weight=2)
    >>> G.add_edge('A', 'C', weight=5)
    >>> vcg_cheapest_path(G, 'A', 'C')
    Path chosen: ['A', 'B', 'C']
    Total cost: 3
    Payment for edge ('A', 'B'): 3.0
    Payment for edge ('B', 'C'): 4.0
    """
    # 1. Find the cheapest path and its total cost
    path = nx.shortest_path(graph, source, target, weight='weight')
    total_cost = nx.shortest_path_length(graph, source, target, weight='weight')
    print(f"Path chosen: {path}")
    print(f"Total cost: {total_cost}")

    # 2. For each edge in that path, compute its VCG payment
    for u, v in zip(path, path[1:]):
        # weight of this edge in the chosen path
        c_e = graph[u][v]['weight']
        # Temporarily remove the edge
        graph_removed = graph.copy()
        graph_removed.remove_edge(u, v)
        try:
            # cost of best path without this edge
            cost_without = nx.shortest_path_length(
                graph_removed, source, target, weight='weight'
            )
        except nx.NetworkXNoPath:
            # if no path exists without this edge, treat cost as infinity
            cost_without = float('inf')
        # VCG payment formula
        payment = cost_without - (total_cost - c_e)
        print(f"Payment for edge ({u!r}, {v!r}): {payment:.1f}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()