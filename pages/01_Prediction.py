import streamlit as st
import pickle
import requests
import re
import pandas as pd
import os
from st_files_connection import FilesConnection
import s3fs


from dotenv import load_dotenv

from preprocessing.preprocessing import preprocess_text, tokenize_text, remove_stopwords, TextPreprocessor, Tokenizer, identity_tokenizer

# Load the environment variables
load_dotenv()

# Configurar las credenciales de AWS
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Configurar la conexión a S3
s3 = s3fs.S3FileSystem(key=aws_access_key_id, secret=aws_secret_access_key)

# access the environment variables
API_KEY = os.getenv("API_KEY")
path_to_pipeline = os.environ.get('PATH_TO_PIPELINE')

# Acceder a la variable de entorno que contiene la ruta al archivo sensible
cloud_storage_path = os.getenv("PATH_TO_PIPELINE_AWS")

# Leer el contenido del archivo desde S3
with s3.open(cloud_storage_path, 'rb') as s3_file:
    loaded_pipeline = pickle.load(s3_file)


# URL de la API para obtener comentarios de un video específico
url = 'https://www.googleapis.com/youtube/v3/commentThreads'


# Inicializa una variable para controlar la visibilidad del formulario
show_form = False

def extract_video_id(link):
    """
    Extrae el ID de un video de YouTube de un enlace de YouTube.
    :param link:
    :return:
    """

    # Utiliza una expresión regular para extraer el ID del video de un enlace de YouTube
    match = re.search(
        r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})',
        link)

    if match:
        return match.group(1)
    else:
        return None


def retrieve_comments(params):
    """
    Realiza una solicitud GET a la API de YouTube para obtener comentarios de un video específico.
    :param params:
    :param url:     URL de la API para obtener comentarios de un video específico
    :param video_id:    ID del video de YouTube
    :param API_KEY:     API_KEY de YouTube
    :param text_format: Formato de texto de los comentarios
    :param max_results: Cantidad máxima de comentarios a obtener
    :return:   DataFrame con los comentarios
    """
    # Realizar la solicitud GET a la API de YouTube
    response = requests.get(url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()

        # Crear una lista para almacenar los comentarios
        comments_list = []

        for item in data['items']:
            comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments_list.append(comment_text)

            # Obtener respuestas a comentarios (si las hay)
            if 'replies' in item.keys():
                replies = item['replies']['comments']
                for reply in replies:
                    reply_text = reply['snippet']['textDisplay']
                    comments_list.append(reply_text)


        # Convertir la lista de comentarios en un DataFrame
        df_comments = pd.DataFrame(comments_list, columns=['Comment'])
        print(df_comments.head())

    else:
        print(f"Error getting comments. Status code: {response.status_code}")

    return df_comments


def execute_pipeline(data):
    """
    Ejecuta el pipeline de preprocesamiento y predicción.
    :param data:   Comentarios de YouTube
    :return:    Predicción de toxicidad
    """

    # Apply the pipeline to the input data
    y_pred = loaded_pipeline.predict(data)
    return y_pred


def apply_row_colors(series, color1, color2):
    """
    Aplica colores a las filas de un DataFrame.
    :param series:  Series del DataFrame
    :param color1:  Color 1
    :param color2:  Color 2
    :return:    Lista de colores para cada fila
    """
    return ['background-color: {}'.format(color1) if i % 2 == 0 else 'background-color: {}'.format(color2)
            for i in range(len(series))]


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

# positioning logo
image = 'yt_logo_name.png'
img_width = 300
img_height = 300

left_co, cent_co,last_co = st.columns([0.3,0.6,0.3])
with left_co:
     st.image(image, width=img_width)

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.subheader("Let\'s predict if the video\'s comments are Toxic or not.")
st.write(" ")
st.write(" ")


# Crea columnas para mostrar la solicitud video y el video de YouTube
col1, col2 = st.columns([0.5,0.5],gap="medium")
with col1:
    # Solicitar al usuario un enlace de YouTube
    st.markdown('##### Enter the YouTube link of the video from which you want to retrieve comments.')
    youtube_link = st.text_input('label ', key='link',
                                 placeholder='Enter the video link here.',
                                 label_visibility= 'collapsed' )

    # Obtener el ID del video de YouTube
    video_id = extract_video_id(youtube_link)

    # Parámetros de la solicitud
    params = {
        'part': 'snippet, replies',
        'videoId': video_id,
        'key': API_KEY,
        'textFormat': 'plainText',  # Puedes cambiar el formato de texto según tus preferencias
        'maxResults': 100,  # Cantidad máxima de comentarios a obtener
    }


    # Verificar si el enlace es válido y se ha introducido alguno
    if youtube_link and video_id:
        st.success("The link is valid.")
        show_form = True
    elif youtube_link:
        st.warning("The link is not valid. Please enter a valid YouTube link.")

with col2:
    # Mostrar el video de YouTube si el enlace es válido
    if 'video_id'  and video_id:
        st.video('https://www.youtube.com/watch?v=' + video_id)

if show_form:
    with st.form('predict_form'):
        submit = st.form_submit_button('GET PREDICTION')
        if submit:
            # Obtener comentarios
            df_comments = retrieve_comments(params)
            prediction = execute_pipeline(df_comments['Comment'])

            # Mapear los valores de la columna "Prediction" a emojis
            prediction_emojis = ["🤬" if pred.any() else "😊" for pred in prediction]

            # Crear un DataFrame con las columnas "Comment" y "Prediction" (con emojis)
            results_df = pd.DataFrame({'Comment': df_comments['Comment'], 'Prediction': prediction_emojis})

            # Mostrar los resultados
            st.subheader('Prediction results for each comment:')
            st.table(results_df.style.apply(lambda row: apply_row_colors(row, '#fdfbf9', '#f8eaec'), axis=0))
            show_form = False
