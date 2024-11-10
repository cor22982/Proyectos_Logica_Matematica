import streamlit as st
st.set_page_config(page_title="Simulador Maquina de Turing", page_icon="🧠")
st.title('Simulador de Maquina de Turing')

st.subheader('Instrucciones')
st.write("<p style='font-size:17px;'>Agregue el archivo de configuracion .yaml para evaluar la maquina de turing</span>", unsafe_allow_html=True)
with st.container():
    # Cargar archivo
    uploaded_file = st.file_uploader("Subir archivo de configuracion", type=["yaml"])
    
    # Si se carga un archivo, mostrar su contenido
    if uploaded_file is not None:
        st.write("Archivo cargado exitosamente:")
        # Mostrar el contenido del archivo dependiendo de su tipo
        if uploaded_file.type == "text/csv":
            import pandas as pd
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            import pandas as pd
            df = pd.read_excel(uploaded_file)
            st.dataframe(df)
        elif uploaded_file.type == "application/pdf":
            st.write("Los archivos PDF no se muestran directamente. Procesa el contenido aquí si es necesario.")
        else:
            st.write(uploaded_file.getvalue().decode("utf-8"))
