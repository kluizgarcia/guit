import streamlit as st
import pandas as pd
import pyodbc


# Função para conectar ao SQL Server
def get_connection():
    server = 'LAPTOP-TPGE99C2\SQLEXPRESS'
    database = 'Base_CL'
    username = 'sa'
    password = '123'

    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(conn_str)
    return conn


# Função para obter dados de uma tabela
def load_data():
    conn = get_connection()
    query = 'select * from login'
    data = pd.read_sql(query, conn)
    conn.close()
    return data


# Título da aplicação
st.title('Exemplo de Conexão com SQL Server')

# Botão para carregar dados
if st.button('Carregar Dados'):
    data = load_data()
    st.write(data)

# Adicione mais funcionalidades conforme necessário
