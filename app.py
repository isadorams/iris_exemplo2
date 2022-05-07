import streamlit as st

st.write("# Classificação de Iris")
st.write("## Exemplo com o comprimento e largura da pétala e sépala")

st.sidebar.write("### Parâmetros")
st.sidebar.slider("Comprimento da sépala", 4.0, 8.0, 5.8, 0.1)
st.sidebar.slider("Largura da sépala", 2.0, 5.0, 3.6, 0.1)
st.sidebar.slider("Comprimento da pétala", 0.9, 7, 3.8, 0.1)
st.sidebar.slider("Largura da pétala", 0.8, 3, 1.4, 0.1)
