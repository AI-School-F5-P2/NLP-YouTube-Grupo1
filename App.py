import streamlit as st


# Configurar la información personalizada en la sección "About"
about_text = """
**YouTube NLP Comments. Grupo 1**

**Coders:**
- Ana Gómez
- Alberto
- Tania Monteiro
- Sandra Gómez S.

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

image = 'YT_logo.png'
img_width = 250
img_height = 250


col1, col2 = st.columns([0.2,0.9],)
with st.container():
    with col1:
        st.image(image, width=img_width)
    with col2:
        st.header("YouTube NLP Comments Prediction App")
        st.subheader('Natural Language Processing.')

col3,col4 = st.columns([0.7,0.3],)
with col3:

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    multi = ''' In the current context of the growing concern over hate messages in video comments on YouTube, 
    the platform faces a significant challenge in maintaining a safe and positive environment for its users. 
    The escalation of these messages has surpassed the capacity of manual moderation, and increasing the moderation 
    team becomes impractical both in terms of cost and scalability.
    
    In response to this issue, YouTube has decided to partner with our consultancy in search of a practical and 
    automated solution to detect hate messages. The goal is to implement an effective tool that can automatically 
    identify these messages, providing a quick and accurate response without relying solely on human intervention.

    This project not only aims to address the increasing prevalence of hate messages but also to find a solution 
    that can adapt and scale efficiently with the constant growth of the platform. The implementation of this 
    solution is essential to maintain a safe, inclusive, and harmful-content-free online environment.
    '''

    st.markdown(multi)
with col4:
    st.write(" ")