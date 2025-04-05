import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def draw_graph_with_walk(graph, walk, title="Random Walk"):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(6, 5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, edge_color='gray', ax=ax)

    # Walk path
    path_edges = list(zip(walk, walk[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=walk, node_color='orange')

    ax.set_title(title)
    st.pyplot(fig)
