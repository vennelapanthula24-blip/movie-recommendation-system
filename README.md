# 🎬 Movie Recommendation System

A simple machine-learning-based movie recommendation system built with **Python, Pandas, Scikit-learn and Streamlit**.

## 🚀 Features

- Select a movie from the dataset
- Recommend similar movies
- Content-based filtering
- TF-IDF text vectorization
- Cosine similarity
- Interactive Streamlit UI
- Displays genre, year, rating and similarity percentage

## 🧠 Machine Learning Approach

The system uses **content-based filtering**.

### Step 1: Combine Features
Movie genres and descriptions are combined into one text field.

### Step 2: TF-IDF
`TfidfVectorizer` converts the text into numerical vectors.

### Step 3: Cosine Similarity
Cosine similarity compares the selected movie with every other movie.

### Step 4: Recommendation
Movies with the highest similarity scores are returned as recommendations.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movies.csv
├── requirements.txt
└── README.md
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🌐 Deploy on Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with GitHub.
4. Select your repository.
5. Select `app.py`.
6. Click Deploy.

## 🛠 Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Streamlit
- Git & GitHub

## 👨‍💻 Author

Vasanth Panthula
