import pandas as pd
import re
import nltk
import seaborn as sns
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


nltk.download('stopwords')
nltk.download('wordnet')

print("Starting Fake News Detection Pipeline...")


print("\nPhase 1: Loading and exploring dataset...")

df_fake = pd.read_csv("fake.csv")
df_true = pd.read_csv("true.csv")

df_fake["label"] = 1   # 1 = Fake news
df_true["label"] = 0   # 0 = Real news
df = pd.concat([df_fake, df_true], axis=0).reset_index(drop=True)

df.drop_duplicates(inplace=True)
df['subject'] = df['subject'].str.lower().str.strip()

print("Class balance:\n", df['label'].value_counts())
print("Phase 1 complete.")


print("\nPhase 2: Preprocessing text...")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)

df['clean_text'] = df['text'].apply(clean_text)


tfidf = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf.fit_transform(df['clean_text'])


svd = TruncatedSVD(n_components=300)
X_reduced = svd.fit_transform(X_tfidf)

X = X_reduced
y = df['label'].values

print("Feature matrix shape:", X.shape)
print("Phase 2 complete.")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nPhase 3: Training SVM model...")

model = SVC(probability=True, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Phase 3 complete.")

print("\nModel Evaluation:")
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - SVM")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.close()
print("fake news data classifier model created by NOOR FATIMA")
print("\nConfusion matrix saved as confusion_matrix.png")
print("Pipeline complete.")
