import streamlit as st

st.title('Meu Primeiro App')
st.write('Bem-vindo ao seu primeiro aplicativo Streamlit')

if st.button('Diga olá'):
    st.write('Olá, mundo!')
