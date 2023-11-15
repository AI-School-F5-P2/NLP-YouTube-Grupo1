import contractions
import pandas as pd
import numpy as np
import spacy
import re
from sklearn.base import BaseEstimator, TransformerMixin




# Setting SpaCy in English
nlp = spacy.load("en_core_web_sm")

# Custom Transformer Class for our text preprocessing function
class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, documents, y=None):
        return self

    def transform(self, x_series):
        # Applying contractions fix
        x_series = x_series.apply(contractions.fix)

        # Applying preprocess function
        x_series = x_series.apply(preprocess_text)

        return x_series

# Custom Transformer Class for tokenization and removing stopwords
class Tokenizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, documents, y=None):
        return self

    def transform(self, x_series):
        # Tokenizing
        x_series = x_series.apply(tokenize_text)

        # Removing Stopwords
        x_series = x_series.apply(remove_stopwords)

        return x_series


# Define a proper function for tokenizer since lambda functions cannot be pickled
def identity_tokenizer(text):
    return text

# Function for preprocessing text
# Pasar a minúsculas, eliminar caracteres especiales
def preprocess_text(text):
    # Convierte todo el texto en a minúsculas
    text = text.lower()

    # reemplaza cualquier carácter no alfanumérico en 'text' con un espacio en blanco.
    text = re.sub(r'\W', ' ', text)

    # Elimina espacios en blanco adicionales
    text = re.sub(r'\s+', ' ', text)

    # Elimina los espacios en blanco al principio y al final de la cadena 'text'.
    text = text.strip()

    # Elimina números
    text = re.sub(r'\d+', '', text)

    # Divide la cadena 'text' en palabras individuales, y luego une estas palabras nuevamente
    # en una cadena con un solo espacio entre cada palabra.
    text = ' '.join(text.split())  # Elimina espacios en blanco adicionales

    return text


# Function for tokenization
# Tokenización del texto
def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

# Función para eliminar las stopwords de un texto tokenizado
def remove_stopwords(text_tokens):
    doc = nlp(" ".join(text_tokens))
    tokens_without_stopwords = [token.text for token in doc if not token.is_stop]
    return tokens_without_stopwords