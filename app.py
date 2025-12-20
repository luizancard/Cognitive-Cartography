import json

import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

# Título Estiloso
st.title("Cognitive Cartography")
st.write("Visualizando a estrutura de dependência do conhecimento.")

# 1. Carregar os Dados
with open("content.json", "r") as f:
    data = json.load(f)

# 2. Criar o Grafo (A Mágica do NetworkX)
G = nx.DiGraph()  # Grafo Direcionado

# Adicionar Nós
for node in data["nodes"]:
    G.add_node(node["id"], label=node["label"], color="red" if node["base"] else "blue")

# Adicionar Conexões (Dependências)
for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"])

# 3. Desenhar na Tela
st.subheader("Mapa de Conceitos: Logaritmos")
fig, ax = plt.subplots(figsize=(8, 6))
pos = nx.spring_layout(G)  # O algoritmo que decide onde cada bolinha fica

# Desenha os nós
colors = [nx.get_node_attributes(G, "color")[node] for node in G.nodes()]
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=colors,
    node_size=2000,
    font_color="white",
    font_size=10,
)

# Mostra o gráfico no Streamlit
st.pyplot(fig)
