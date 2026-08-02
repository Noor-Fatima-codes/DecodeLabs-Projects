import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EXIT_COMMANDS = ["exit", "quit", "bye"]

df = pd.read_csv("raw_skills.csv")

print("=" * 55)
print("  Welcome to TechMatch | Tech Stack Recommender")
print("  Built by Noor Fatima | DecodeLabs Project 3")
print("=" * 55)

print("\nAvailable job roles in the dataset:")
print(df["job_role"].tolist())
print("-" * 55)


def recommend(user_skills):
    """Given a list of skills, return the top 3 matching job roles."""
    user_profile = " ".join(user_skills)

    all_text = df["skills"].tolist() + [user_profile]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)

    user_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()

    df_copy = df.copy()
    df_copy["similarity"] = similarity_scores
    return df_copy.sort_values(by="similarity", ascending=False).head(3)

while True:
    print("\nEnter at least 3 of your skills (comma separated)")
    print("Example: Python, Cloud, Automation")
    print("(Type 'exit' anytime to quit)")

    user_input = input("Your skills: ").strip()

    if user_input.lower() in EXIT_COMMANDS:
        print("\nThanks for using TechMatch! Goodbye, and good luck on your career path.")
        break

    user_skills = [skill.strip() for skill in user_input.split(",") if skill.strip()]

    if len(user_skills) < 3:
        print("Please enter at least 3 skills for accurate matching.")
        continue

    top_matches = recommend(user_skills)

    print("\nTop 3 Recommended Career Paths:")
    for rank, (_, row) in enumerate(top_matches.iterrows(), start=1):
        print(f"{rank}. {row['job_role']}  (Match Score: {row['similarity']:.2f})")