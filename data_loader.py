import streamlit as st
import pandas as pd

# Permitir que o usuário faça upload de um arquivo CSV
#uploaded_file = st.file_uploader('Escolha um arquivo CSV', type='csv')

#if uploaded_file is not None:
#    data = pd.read_csv(uploaded_file, sep=';')
#    st.write(data)

data = pd.read_csv('/workspaces/streamlit-testes/TradeInformationConsolidatedFile_20240712_1 (1).csv', sep=';')
st.write(data)
