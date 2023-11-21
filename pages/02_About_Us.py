import streamlit as st


# Configurar la información personalizada en la sección "About"
about_text = """
**YouTube NLP Comments. Grupo 1**

**Coders:**
- Ana Milena Gómez Giraldo
- Alberto Rodríguez Vaquero
- Tania Monteiro Vitoria
- Sandra Gómez Santamaría.

[Repositorio del proyecto](https://github.com/AI-School-F5-P2/NLP-YouTube-Grupo1.git)
"""
# Page Configuration
st.set_page_config(
    page_title="YouTube NLP Predict App",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': about_text
    }
)

# positioning logo
image = 'yt_logo_name.png'
img_width = 350
img_height = 350

left_co, cent_co,last_co = st.columns([0.3,0.6,0.3])
with cent_co:
     st.image(image, width=img_width)

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

col3,col4, col5 = st.columns([0.1,0.6,0.2],)
with col4:
    st.markdown("## Project")
    st.write(" ")
    st.markdown("##### :notebook: NLP project from Factoria F5's AI Bootcamp ")
    st.write(" ")
    st.write(" ")

    st.markdown("## Meet the Team")
    st.write(" ")
    st.markdown("#### :sparkles: [Ana Milena Gómez Giraldo](https://www.linkedin.com/in/ana-milena-gomez-giraldo/)")
    st.markdown("#### :sparkles: [Alberto Rodríguez Vaquero](https://www.linkedin.com/in/alberto-rodriguez-vaquero-a81071134/)")
    st.markdown("#### :sparkles: [Tania Monteiro Vitoria](https://www.linkedin.com/in/taniamonvit/)")
    st.markdown("#### :sparkles: [Sandra Gómez Santamaría](https://www.linkedin.com/in/sandragomezs/)")

    st.write(" ")
    st.write(" ")

    st.markdown("## Repository")
    st.write(" ")
    st.markdown("#### :computer: [GitHub](https://github.com/AI-School-F5-P2/NLP-YouTube-Grupo1.git)")

