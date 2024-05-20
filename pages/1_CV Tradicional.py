import streamlit as st

st.write("# CV Tradicional")

with open("CV de una hoja.pdf", "rb") as pdf_file:
    cv_1_hoja = pdf_file.read()

st.download_button("Descargar CV de una Hoja", data=cv_1_hoja, file_name= 'CV Jorge Saenz de Miera.pdf', mime='pdf')