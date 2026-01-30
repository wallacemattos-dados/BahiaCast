import streamlit as st

def date_filter():
    col1, col2 = st.columns(2)
    with col1:
        month = st.selectbox("Mês", range (1, 13))
    with col2:
        year = st.selectbox("Ano", range (1980, 2005))
    return month, year