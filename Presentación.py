import streamlit as st

col_111, col_222 = st.columns(2)
col_222.page_link("pages/1_Currículum.py", label="Ir a Currículum 🡺")
col_222.page_link("pages/2_Blog.py", label="Ir a Blog 🡺")

col_1, col_2 = st.columns(2)
col_1.write("# Jorge Sáenz de Miera Marzo")
col_2.image('Foto Perfil.png', width=170)

col_11, col_22 = st.columns(2)
col_11.write("**jorgesaenzdemiera2@gmail.com**")
col_11.write('**(+34) 638881681**')
col_22.write('[**Linkedin**](https://www.linkedin.com/in/jorgesaenzdemiera/)')
col_22.write('**Cercedilla, Madrid, España**')

st.write("## Sobre Mi")
st.write('Soy estudiante del último año de la carrera de Ciencia de Datos e Inteligencia Artificial en la Universidad Politécnica de Madrid (UPM). Durante estos 4 años he podido desarrollar un sólido conocimiento en técnicas avanzadas de análisis de datos, machine learning y deep learning.')
st.write('Actualmente, estoy completando mis prácticas en el Departamento de Inteligencia Artificial de Inetum, donde he tenido la oportunidad de aplicar mis habilidades en proyectos reales, trabajando con datos y desarrollando modelos predictivos. Esta experiencia me ha permitido fortalecer mis competencias técnicas y aprender a trabajar en equipo en un entorno profesional.')
st.write('Soy una persona tranquila y adaptable, capaz de enfrentarme a cualquier situación con serenidad. Me gusta resolver problemas utilizando el pensamiento crítico, y siempre analizo cada situación para tomar las mejores decisiones posibles. Estoy siempre en busca de nuevos desafíos que me permitan seguir creciendo profesional y personalmente.')

st.write("\n")
st.write("\n")
st.write("**Carta de Motivación Capgemini:**")
with open("Carta de Presentación.pdf", "rb") as pdf_file:
    carta_presentacion = pdf_file.read()
st.download_button("Descargar Carta de Motivación para Capgemini", data=carta_presentacion, file_name= 'Carta de Motivación.pdf', mime='pdf')

