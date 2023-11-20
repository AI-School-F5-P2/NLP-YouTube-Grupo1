# YouTube Hate Speech Detection

## Overview
The YouTube Hate Speech Detection project aims to tackle the growing concern of hate speech within video comments on the platform. Faced with the limitations of the existing moderation team and the impracticality of scaling, YouTube has outsourced the challenge to our consulting firm. The goal is to implement an automated solution for detecting hate speech, allowing prompt actions such as content removal or user banning.

The emphasis is on a practical implementation, prioritizing efficiency over precision.

## Solution Description
Our solution involves developing a Natural Language Processing (NLP) model capable of automatically detecting hate speech in YouTube comments. The practicality of the solution is paramount, ensuring a fast and scalable approach to handle the increasing volume of offensive messages.

## Implementation Details

### Data Collection
We collected a diverse dataset containing labeled hate speech and non-offensive comments, crucial for training and evaluating our model.

### Preprocessing
Data preprocessing tasks, including tokenization, stop word removal, and lemmatization, will be performed to prepare the data for modeling.

### Model Choice
We employed different NLP models such as AdaBoost, GradientBoost, RandomForest, Logistic Regression, LGB, KNN but we finally decided to go with the one that gaves us the best and most efficient results and that was MultinomiaNB.

### Training and Evaluation
The model was trained on the collected dataset, and its performance will be evaluated using various metrics, ensuring it generalizes well to new comments.

### Deployment
The model was deployed in a production environment, potentially leveraging cloud services for scalability and integration with YouTube's comment system.

## Repository Structure

- **README.md:** Project usage guide.
- **requirements.txt:** Install this file to ensure your environment has all the necessary libraries. You can install it by running "pip install -r requirements.txt" in the terminal.
- **.gitignore:** Prevents selected files and folders from being uploaded to the repository.

### Code Files

- **youtube_hate_detection.py:** Interface for detecting hate speech in YouTube comments.
- **Performance_Report.md:** Classification report explaining the AI's capability.

### Notebooks

- **EDA.ipynb:** Exploratory data analysis.
- **Hyperparameter_tuning.ipynb:** Search for the best hyperparameters for the final model.
- **Modelling.ipynb:** Training the final chosen model and creating the pickle.
- **Model_comparison.ipynb:** Model comparison to determine which one provides the best metrics.

## Installation and Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages by running "pip install -r requirements.txt" in the terminal.
4. Run the YouTube Hate Speech Detection app using the provided scripts.

## Contributing

If you'd like to contribute, please fork the repository, make your changes, and open a pull request following the outlined process in the README.md.


**Fork the Project → Create your Feature Branch → Commit your Changes → Push to the Branch → Open a Pull Request**
