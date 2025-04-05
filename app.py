import streamlit as st
from graph_utils import batched_random_walk
from visualize import draw_graph_with_walk

# Sample graph
sample_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

st.title("🎯 Random Walks on Graph - Visualizer")
st.markdown("Built by Vyaishnavi ✨")

# Sidebar Controls
start_node = st.selectbox("Start Node", list(sample_graph.keys()))
walk_length = st.slider("Walk Length", 2, 20, 5)
batch_size = st.slider("Number of Walks", 1, 10, 3)

# Walk Simulation
if st.button("Simulate Random Walks"):
    walks = batched_random_walk(sample_graph, start_node, walk_length, batch_size)

    for i, walk in enumerate(walks):
        st.subheader(f"Walk {i+1}")
        st.text(" ➡️ ".join(walk))
        draw_graph_with_walk(sample_graph, walk, title=f"Walk {i+1}")
