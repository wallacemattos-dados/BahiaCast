import streamlit as st
import streamlit.components.v1 as components
from services.data_loader import load_data, filter_data
from ui.filters import date_filter

st.set_page_config(page_title="BahiaCast",
                   page_icon="🎵",
                    layout="wide")

st.title("📻 BahiaCast - Top Charts")
st.markdown("Descubra as músicas que marcaram época.")
st.divider()

df = load_data()
month, year = date_filter()
filtered = filter_data(df, month, year)

if filtered.empty:
    st.warning("Nenhuma música encontrada")
else:
    for _, row in filtered.iterrows():

        with st.container(border=True):
            col_info, col_player = st.columns([0.7, 0.3])

            with col_info:
                st.write("")
                st.subheader(f"#{row['rank']} {row['title']}")
                st.text(f"🎤 {row['artist']}")

            with col_player:
                components.iframe(row['spotify_url'], height=80)