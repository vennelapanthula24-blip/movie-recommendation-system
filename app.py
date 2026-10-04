import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load movie data
movies = pd.read_csv("movies.csv")

# Fill empty values
movies["genres"] = movies["genres"].fillna("")
movies["overview"] = movies["overview"].fillna("")

# Combine movie information
movies["features"] = movies["genres"] + " " + movies["overview"]

# Convert text into numbers
vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform(movies["features"])

# Calculate similarity
similarity = cosine_similarity(matrix)


# -----------------------------
# Simple UI
# -----------------------------

st.title("Movie Recommendation System")

st.write("Select a movie to get similar movie recommendations.")

st.write("")

# Select movie
selected_movie = st.selectbox(
    "Select Movie:",
    movies["title"]
)

# Button
if st.button("Recommend Movies"):

    movie_index = movies[movies["title"] == selected_movie].index[0]

    scores = list(enumerate(similarity[movie_index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    st.subheader("Recommended Movies")

    for i, score in scores[1:6]:

        st.write("Movie:", movies.iloc[i]["title"])
        st.write("Genre:", movies.iloc[i]["genres"])
        st.write("Year:", movies.iloc[i]["year"])
        st.write("Rating:", movies.iloc[i]["rating"])

        st.write("-------------------------")