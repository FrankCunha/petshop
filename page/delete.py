import streamlit as st
import controller.cliente as cliente

def Deletar():
    st.title('Deletar Dados')
    with st.form(key='delete'):
        nomecliente = st.text_input(label='Insira o nome: ')
        buttom_submit = st.form_submit_button('Deletar')
    if buttom_submit:
        cliente.excluir(nomecliente)
        st.success('Cliente deletado com Sucesso!')