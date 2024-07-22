from datetime import time
import streamlit as st 
import pandas as pd 
import requests 

# Função para obter dados financeiros em tempo real 
#@st.cache(allow_output_mutation=True) 

def get_realtime_data(): 
    response = requests.get("https://api.financedata.com/price") 
    data = response.json() 
    return pd.DataFrame(data) 

# Criando uma função que atualiza os dados a cada 30 segundos 
def stream_data(): 
    df = get_realtime_data() 
    while True: 
        st.write(df) 
        time.sleep(30) 
        df = get_realtime_data() 
        
stream_data()
