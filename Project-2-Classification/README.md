# Project 2: Data Classification Using AI

## Goal
Build a classification model that can categorize data based on patterns learned
from training data, demonstrating the fundamentals of supervised learning.

## Key Requirements
- Load and understand a dataset
- Split data into training and testing sets
- Apply a classification algorithm
- Evaluate model performance

## Key Skills Practiced
Data handling, text preprocessing, supervised learning, model evaluation

## Project Used: Fake News Detection
Instead of a basic dataset, this project applies the classification pipeline
to a real-world problem detecting fake vs. real news articles using
Natural Language Processing (NLP) and Machine Learning.

## How It Works
1. **Dataset** — Combined fake news and true news articles, labeled 1 (fake)
   and 0 (real).
2. **Preprocessing** — Text is cleaned (lowercased, punctuation removed,
   stopwords removed, lemmatized) using NLTK.
3. **Feature Extraction** — TF IDF converts text into numeric vectors,
   and TruncatedSVD reduces dimensionality for faster training.
4. **Train-Test Split** — 80% training, 20% testing, stratified by label.
5. **Model** — A Support Vector Machine (SVM) classifier is trained on the
   processed features.
6. **Evaluation** — Accuracy, Precision, Recall, and F1 Score are calculated,
   along with a Confusion Matrix visualized as a heatmap.

## How to Run
```bash
pip install pandas scikit learn nltk seaborn matplotlib
python fake_news_classifier.py
```

**Note:** Requires `fake.csv` and `true.csv` dataset files in the same folder.

