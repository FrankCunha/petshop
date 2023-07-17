import streamlit as st

import controller.cliente as cliente


def consultar():
    st.title('Consultar Dados')
    colunas = st.columns((1,2,1,2,1,2,1,2,1,2))
    campos = ['nomecliente', 'sexocliente', 'cpf', 'endereço', 'telefone', 'especiedeanimal', 'raçamultaçãoanimal', 'idadedoanimal', 'sexoanimal']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in cliente.selecionar():
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns((1,2,1,2,1,2,1,2,1,2))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        col5.write(item[4])
        col6.write(item[5])
        col7.write(item[6])
        col8.write(item[7])
        col9.write(item[8])
        col10.write(item[9])
        
            