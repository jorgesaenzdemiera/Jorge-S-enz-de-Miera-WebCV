import streamlit as st

col_1, col_2 = st.columns(2)
col_1.page_link("pages/1_Currículum.py", label="🡸 Ir a Currículum")
col_1.page_link("Presentación.py", label="🡸 Ir a Presentación")

st.write("# Entrada de Blog divulgativo")
