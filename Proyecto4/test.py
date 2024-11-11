import streamlit as st
import yaml

# Crear un diccionario como ejemplo de contenido YAML
data = {
    'config': {
        'setting1': 'value1',
        'setting2': 'value2'
    }
}

# Convertir el diccionario a una cadena YAML
yaml_content = yaml.dump(data)

# Crear el botón de descarga
st.download_button(
    label="Descargar archivo YAML",
    data=yaml_content,
    file_name="config.yaml",
    mime="text/plain"
)
