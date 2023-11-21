# YouTube Hate Speech Detection

## Overview
The YouTube Hate Speech Detection project aims to tackle the growing concern of hate speech within video comments on the platform. Faced with the limitations of the existing moderation team and the impracticality of scaling, YouTube has outsourced the challenge to our consulting firm. The goal is to implement an automated solution for detecting hate speech, allowing prompt actions such as content removal or user banning.

The emphasis was on a practical implementation, prioritizing efficiency over precision.

## Solution Description
Our solution involves developing a Natural Language Processing (NLP) model capable of automatically detecting hate speech in YouTube comments. The practicality of the solution is paramount, ensuring a fast and scalable approach to handle the increasing volume of offensive messages.

## Implementation Details

### Data Collection
We collected a diverse dataset containing labeled hate speech and non-offensive comments, crucial for training and evaluating our model.

### Preprocessing

Data preprocessing tasks have been performed, such as converting text to lowercase, removing special characters, whitespace, and numbers; also, text tokenization, removal of stopwords, and vectorization

### Model Choice
We employed different Machine Learning algorithms such as AdaBoost, GradientBoost, RandomForest, Logistic Regression, LGB, KNN but we finally decided to go with the one that gaves us the best and most efficient results: MultinomiaNB.

### Training and Evaluation
The model has been trained on the collected dataset, and its performance will be evaluated using various metrics, ensuring it generalizes well to new comments.

### Deployment
The model has been deployed in a production environment, leveraging cloud services for scalability and integration with YouTube's comment system.

## Repository Structure

- **`README.md`:** Project usage guide.
- **`requirements.txt`:** Install this file to ensure your environment has all the necessary libraries. You can install it by running "pip install -r requirements.txt" in the terminal.
- **`.gitignore`:** Prevents selected files and folders from being uploaded to the repository.

### Code Files

- **`App.py`:** Interface for detecting hate speech in YouTube comments.
- **`01_Prediction.py`:** Prediction script for the final model.
- **`02_About_Us.py`:** About us script.
- **`preprocessing.py`:** Preprocessing functions.


### Notebooks

- **`Preprocesado+Modelo.ipynb`:** Preprocessing and model training.
- **`Embeddings.ipynb`:** Embeddings encoding and neural network training.


## Installation and Usage

1. Clone the repository (https://github.com/AI-School-F5-P2/NLP-YouTube-Grupo1.git)
2. Navigate to your project directory.
3. Install the required packages by running `pip install -r requirements.txt` in the terminal.
4. Run the YouTube Hate Speech Detection App using the command `streamlit run App.py` in the terminal.


