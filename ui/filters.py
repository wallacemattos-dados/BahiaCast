import streamlit as st

def date_filter():
    st.sidebar.header("🎚️ Filtros")
    month = st.selectbox("Mês", range (1, 7))
    year = st.selectbox("Ano", range (1998, 2000))

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Sobre")
    st.sidebar.info("Este dashboard exibe o Top 10 da Billboard filtrado por data.")
    
    return month, year