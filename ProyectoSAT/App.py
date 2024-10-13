
"""
Integrantes:
• Gustavo Adolfo Cruz Bardales - 22779
• Javier Andrés Chen González - 22153
• Josué Emanuel Say Garcia - 22801
• Pedro Pablo Guzmán Mayén - 22111
• Mathew Alexander Cordero Aquino - 22982
• Sebastián Estrada Tuch - 21405

"""

import streamlit as st
from Parser import parseToString
from Algoritm_set import Ejecute_Algoritm
# Configura la página de la aplicación con un título y un ícono
st.set_page_config(page_title="Evaluador lógico", page_icon="🧠")
st.title('Evaluador de Expresiones Lógicas')


if 'expression_input' not in st.session_state:
    st.session_state.expression_input = ''


operators = {'∨': ' ∨ ', '∧': ' ∧ ', '¬': '¬'}


col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button('∨'):
        st.session_state.expression_input += operators['∨']
with col2:
    if st.button('∧'):
        st.session_state.expression_input += operators['∧']
with col3:
    if st.button('¬'):
        st.session_state.expression_input += operators['¬']


predefined_expressions = [
    'p ∧ ¬p', 
    'q ∨ p ∨ ¬p', 
    '(¬p ∨ ¬r ∨ ¬s) ∧ (¬q ∨ ¬p ∨ ¬s)', 
    '(¬p ∨ ¬q) ∧ (q ∨ ¬s) ∧ (¬p ∨ s) ∧ (¬q ∨ s)',
    '(¬p ∨ ¬q ∨ ¬r) ∧ (q ∨ ¬r ∨ p) ∧ (¬p ∨ q ∨ r)',
    'r ∧ (¬q ∨ ¬r) ∧ (¬p ∨ q ∨ ¬r) ∧ q'
]


col1, col2 = st.columns([3,2])
with col1:
    selected_expression = st.selectbox('Usar una expresión del documento', [''] + predefined_expressions)
with col2:
    expression_input = st.text_input('Ingresa la expresión manualmente', st.session_state.expression_input)


st.session_state.expression_input = expression_input


expression = expression_input if expression_input else selected_expression


algoritmo = st.selectbox('Selecciona el Algoritmo', ['Fuerza Bruta', 'DPL'])


if st.button('Evaluar'):
    if expression:
        result, asignacion = Ejecute_Algoritm(expression, algoritmo)
        if result:
            st.success('La expresión es satisfacible 😃')
            if algoritmo == 'Fuerza Bruta':
                st.write('Asignación:', parseToString(asignacion))
            elif algoritmo == 'DPL':
                st.write('Asignación:', asignacion)
        else:
            st.error('La expresión no es satisfacible 😞')
    else:
        st.warning('Por favor ingresa una expresión lógica válida.')


if 'result' in locals():
    if result:
        st.markdown("### ¡La expresión es **satisfacible**!")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwebstockreview.net%2Fimages%2Fclipart-smile-smile-gif-2.gif&f=1&nofb=1&ipt=294231fe86a240d4509d6ae34b13cff3bc32cee00995943d15638eb2239d3d8f&ipo=images", width=200)
    else:
        st.markdown("### La expresión **no** es satisfacible.")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fimages%2Ffc1d577e8b42f847e1ef1615b76a9483%2Ftenor.gif&f=1&nofb=1&ipt=46395077f203095ad2f2bb4fd4e8d16027782772c5832057cba83ad55ee6155e&ipo=images", width=200)
