import streamlit as st
from api_client import get_graph
from pyvis.network import Network

st.header("🕸 Knowledge Graph")

data = get_graph()

net = Network(height="600px", directed=True)

for node in data["nodes"]:
    net.add_node(node["id"], label=node["label"])

for edge in data["edges"]:
    net.add_edge(edge["from"], edge["to"], label=edge["type"])

net.save_graph("kg.html")

st.components.v1.html(open("kg.html").read(), height=650)
