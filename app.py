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
    page_icon="🛫",
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
        st.header("Proyecto YouTube NLP Comments")
        st.subheader('Natural Language Processing.')


st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
multi = ''' En el contexto actual de la creciente preocupación por los mensajes de odio en los comentarios de videos en
YouTube, la plataforma se enfrenta a un desafío significativo para mantener un entorno seguro y positivo para sus 
usuarios. La escalada de estos mensajes ha superado la capacidad de moderación manual, y aumentar el equipo resulta 
impracticable tanto en términos de costo como de escalabilidad.

Ante esta problemática, YouTube ha decidido asociarse con nuestra consultora en busca de una solución práctica y 
automatizada para detectar mensajes de odio. El objetivo es implementar una herramienta eficaz que permita identificar 
automáticamente estos mensajes, ofreciendo una respuesta rápida y precisa sin depender exclusivamente de la 
intervención humana.

Este proyecto no solo busca abordar la creciente concurrencia de mensajes de odio, sino también encontrar una solución 
que pueda adaptarse y escalar eficientemente con el constante crecimiento de la plataforma. La implementación de esta 
solución es esencial para mantener un entorno en línea seguro, inclusivo y libre de contenido perjudicial.
'''
st.markdown(multi)