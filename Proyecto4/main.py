import streamlit as st
import yaml
from reader import Reader
from TM import TM
st.set_page_config(page_title="Simulador Maquina de Turing", page_icon="🧠")
st.title('Simulador de Maquina de Turing')
st.subheader('Instrucciones')
st.write("<p style='font-size:17px;'>Agregue el archivo de configuracion .yaml para evaluar la maquina de turing</span>", unsafe_allow_html=True)


with st.container():
    # Cargar archivo
    uploaded_file = st.file_uploader("Subir archivo de configuración", type=["yaml"])
    if uploaded_file is not None:
        st.write("Archivo cargado exitosamente:")
        try:
            content = yaml.safe_load(uploaded_file)
            lector = Reader(content=content)
            maquina = TM(lector=lector)
            result, historial = maquina.simulate(lector.cadena)
            re= f"De la cadena \"{lector.cadena}\" se llego al estado de: \"{result}\""
            st.subheader('Resultado cadena')
            if result == "rechazo":
                st.error(re)
            elif result == "aceptado":
                st.success(re)
            else:
                st.warning(re)
            pasos = ''
            for p in historial:
                pasos += f'{p}<br>'
            st.subheader('Configuraciones de la cinta')
            st.write(f"<span style='font-size:20px; font-style:italic;'>{pasos}</span>", unsafe_allow_html=True)
            st.subheader('Digrama de la Maquina de Turing')
            maquina.graph()
            st.image('../graphs/maquina_turing.png')
            
        except yaml.YAMLError as e:
            st.error(f"Error al leer el archivo YAML: {e}")
