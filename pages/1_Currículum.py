import streamlit as st


col_1, col_2 = st.columns(2)

col_1.write("\n")
col_1.write("\n")
col_1.write("# Currículum")
col_2.image('Foto Perfil.png', width=170)

st.write("## Experiencia Laboral")
st.write("- **Inetum Consulting,** Madrid: *Becario*")
md = '<p style="font-size: 11px;">FEBRERO 2024 - JUNIO 2024</p>'
st.markdown(md, unsafe_allow_html=True)
col_11, col_22 = st.columns(2)
col_11.write("Trabajé en el Departamento de Inteligencia Artificial para desarrollar un sistema de Predicción de Incidencias")
col_22.link_button("Google Collab con parte del trabajo realizado", "https://colab.research.google.com/drive/1PT6RTLH4xDiAIlG6_h6RvL3qbNnmqROF?usp=sharing")

st.write("## Formación")
st.write("- **Universidad Politécnica de Madrid (ETSIINF),** Madrid: *Grado en Ciencia de Datos e Inteligencia Artificial*")
md = '<p style="font-size: 11px;">SEPTIEMBRE 2020 - JUNIO 2024</p>'
st.markdown(md, unsafe_allow_html=True)

st.write("\n")
st.write("## Proyectos realizados en la Universidad")
st.write("- **ETL con Kafka:** abril 2023")
col_111, col_222 = st.columns(2)
col_111.write("Diseño y desarrollo de un sistema que extrae, procesa y carga un flujo de datos en tiempo real. Realizado en grupo con el uso de Apache Kafka y MySQL.")
col_222.write("\n")
col_222.link_button("GitHub", "https://github.com/jorgesaenzdemiera/ETL_LOGS_APACHE")
st.write("- **Recomendador de canciones de Spotify:** mayo 2023")
col_1111, col_2222 = st.columns(2)
col_1111.write("Diseño y desarrollo de un sistema en el que el usuario elige visualmente sus canciones favoritas para que se genere una recomendación de otras canciones en función de los gustos de otros usuarios. Realizado en grupo con el uso de Java, Docker y Python")
col_2222.write("\n")
col_2222.write("\n")
col_2222.write("\n")
col_2222.link_button("GitHub", "https://github.com/jorgesaenzdemiera/si-spotify-recommender")
st.write("- **Integración de datos médicos:** marzo 2023")
col_11111, col_22222 = st.columns(2)
col_11111.write("Armonización de datos de distintos hospitales en una única base de datos común, monitorizando cada dato. Realizado en grupo con el uso de Python y MySQL")
col_22222.write("\n")
col_22222.link_button("GitHub", "https://github.com/jorgesaenzdemiera/ETL_LOGS_APACHE")

st.write("\n")
st.write("## Idiomas")
st.markdown("""
            - **Español:** Idioma Nativo
            - **Inglés:** Nivel Intermedio Alto (B2)
         """)

st.write("\n")
st.write("\n")
st.write("## Conóceme más:")
with open("CV Jorge Sáenz de Miera.pdf", "rb") as pdf_file:
    cv_tradicional = pdf_file.read()

with open("CV Infografico.pdf", "rb") as pdf_file:
    cv_infografico = pdf_file.read()


col_111111, col_222222, col_333333 = st.columns(3)
col_111111.download_button("Descargar CV Tradicional", data=cv_tradicional, file_name= 'CV Jorge Saenz de Miera.pdf', mime='pdf')

col_222222.download_button("Descargar CV Infográfico", data=cv_infografico, file_name= 'CV Jorge Saenz de Miera Infografico.pdf', mime='pdf')

col_333333.link_button("Ver Vídeo Currículum", "https://drive.google.com/file/d/1UvLhyMcfIs1ALCr04Gvhbt-HhnkiDpud/view?usp=sharing")