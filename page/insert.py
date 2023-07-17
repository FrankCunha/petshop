import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    animais = ['cachorro', 'gato', 'passaro', 'coelho', 'peixe', 'porquinho da india', 'hamster']
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome:')
        input_sexo = st.text_input(label='Insira o sexo: ')
        input_cpf = st.text_input(label='Insira o CPF: ')
        input_end = st.text_input(label='Insira o endereço: ')
        input_cell = st.text_input(label= 'insira o numero de telefone: ')
        input_animal = st.selectbox(label='Insira a espécie do animal: ', options=animais)
        input_raça = st.text_input(label= 'Insira a raça/multação ou cor do animal: ')
        input_idade = st.number_input(label='Insira a idade do animal: ', format='%d', step=1)
        input_sexoanimal = st.text_input(label='Insira o sexo do animal: ')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_sexo, input_cpf, input_end, input_cell, input_animal, input_raça, input_idade, input_sexoanimal)
            st.success('Cadastro concluido com sucesso!')