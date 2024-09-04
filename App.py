import streamlit as st
from Parser import infix_to_Postfix, Parser, fuerzaBruta, parseToNumber, parseToString

# Configuración de la página
st.set_page_config(page_title="Evaluador lógico", page_icon="🧠")
st.title('Evaluador de Expresiones Lógicas')

operators = {'∨': ' ∨ ', '∧': ' ∧ ', '¬': '¬'}

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button('∨'):
        st.session_state.expression += operators['∨']
with col2:
    if st.button('∧'):
        st.session_state.expression += operators['∧']
with col3:
    if st.button('¬'):
        st.session_state.expression += operators['¬']

expression = st.text_input('Ingresa la expresión lógica', '(p ∨ q) ∧ (q ∨ s)', key='expression')

if st.button('Evaluar'):
    if expression:
        postfix_expr = infix_to_Postfix(expression)
        parsed_expr = Parser(postfix_expr)

        result, asignacion = fuerzaBruta(parseToNumber(parsed_expr))

        if result:
            st.success('La expresión es satisfacible 😃')
            st.write('Asignación:', parseToString(asignacion))
        else:
            st.error('La expresión no es satisfacible 😞')
    else:
        st.warning('Por favor ingresa una expresión lógica válida.')

# Visualización adicional con emojis
if 'result' in locals():
    if result:
        st.markdown("### ¡La expresión es **satisfacible**!")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwebstockreview.net%2Fimages%2Fclipart-smile-smile-gif-2.gif&f=1&nofb=1&ipt=294231fe86a240d4509d6ae34b13cff3bc32cee00995943d15638eb2239d3d8f&ipo=images", width=200)
    else:
        st.markdown("### La expresión **no** es satisfacible.")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fimages%2Ffc1d577e8b42f847e1ef1615b76a9483%2Ftenor.gif&f=1&nofb=1&ipt=46395077f203095ad2f2bb4fd4e8d16027782772c5832057cba83ad55ee6155e&ipo=images", width=200)

