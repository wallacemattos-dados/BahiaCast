import streamlit as st
from services.data_loader import load_data, filter_data
from ui.filters import date_filter

st.set_page_config(page_title="BahiaCast",
                   page_icon="🎵",
                    layout="wide")
st.title("BahiaCast - Rádio")

df = load_data()
month, year = date_filter()
filtered = filter_data(df, month, year)

if filtered.empty:
    st.warning("Nenhuma música encontrada")
else:
    for _, row in filtered.iterrows():
        st.subheader(f"#{row['rank']} — {row['title']}")
        st.text(row['artist'])
        st.markdown(f"[▶️ Ouvir no Spotify]({row['spotify_url']})")
        st.divider()