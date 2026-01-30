import streamlit as st

def date_filter():
    col1, col2 = st.columns(2)
    with col1:
        month = st.selectbox("Mês", range (1, 7))
    with col2:
        year = st.selectbox("Ano", range (1998, 2000))
    return month, year