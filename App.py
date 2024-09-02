import streamlit as st
from Parser import infix_to_Postfix, Parser, fuerzaBruta, parseToNumber, parseToString

st.set_page_config(page_title="Evaluador lógico",page_icon="🧠")
st.title('Evaluador de Expresiones Lógicas')

expression = st.text_input('Ingresa la expresión lógica', '(p ∨ q) ∧ (q ∨ s) ∧ (p ∨ s) ∧ (q ∨ s)')

if st.button('Evaluar'):
    if expression:
        postfix_expr = infix_to_Postfix(expression)
        parsed_expr = Parser(postfix_expr)

        result, asignacion = fuerzaBruta(parseToNumber(parsed_expr))

        if result:
            st.success('La expresión es satisfacible')
            st.write('Asignación:', parseToString(asignacion))
        else:
            st.error('La expresión no es satisfacible')
    else:
        st.warning('Por favor ingresa una expresión lógica válida.')

