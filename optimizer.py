import networkx as nx
import pandas as pd

routes = pd.read_csv("routes.csv")

def optimize_route(destinations):
    G = nx.Graph()

    for _, row in routes.iterrows():
        G.add_edge(row["From"], row["To"], weight=row["Hours"])

    optimized = []
    for i in range(len(destinations)-1):
        path = nx.shortest_path(
            G,
            source=destinations[i],
            target=destinations[i+1],
            weight="weight"
        )
        optimized.extend(path[:-1])
    optimized.append(destinations[-1])

    return optimized