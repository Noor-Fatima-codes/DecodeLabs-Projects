# Project 3: AI Recommendation Logic - Tech Stack Recommender

## Goal
Build a recommendation system that maps a user's skills to the most relevant
job roles, using Content-Based Filtering with similarity logic.

## Key Requirements
- Take user input (minimum 3 skills)
- Match preferences using similarity logic
- Display recommended items (Top 3 job roles)
- Runs in a continuous loop until the user exits

## Key Skills Practiced
Logic building, pattern matching, recommendation concepts, TF-IDF, Cosine Similarity

## How It Works
1. **Dataset** — `raw_skills.csv` contains job roles and their associated skills,
   treated as the "items" in the recommendation engine.
2. **Ingestion** — The user enters at least 3 skills (comma separated).
3. **Vector Mapping** — User skills and job role skills are converted into
   numeric vectors using TF-IDF, so both share the same vocabulary space.
4. **Scoring** — Cosine Similarity measures the "angle" between the user's
   skill vector and each job role's vector, producing a match score between 0 and 1.
5. **Sorting & Filtering** — Job roles are sorted by similarity score, and
   only the Top 3 highest scoring matches are displayed.
6. **Continuous Loop** — The program keeps asking for skills until the user
   types `exit`, `quit`, or `bye`.

## How to Run
```bash
pip install pandas scikit learn
python tech_stack_recommender.py
```

**Note:** Requires `raw_skills.csv` in the same folder.

## Example
```
Your skills: Python, Cloud, Automation

Top 3 Recommended Career Paths:
1. Sys Admin           (Match Score: 0.37)
2. Cloud Architect     (Match Score: 0.34)
3. DevOps Engineer     (Match Score: 0.32)
```
## Output Screenshot
![Tech Stack Recommender Output](./project%203%20output.jpeg)
