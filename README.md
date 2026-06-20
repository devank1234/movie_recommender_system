# 🎬 Movie Recommender System

A content-based Movie Recommendation System built using Python, Pandas, Scikit-Learn, and Streamlit. The system recommends movies similar to a user's selected movie by analyzing movie metadata and calculating similarity scores using vectorization techniques.

## 📌 Project Overview

This project uses the TMDB 5000 Movies Dataset to recommend movies based on content similarity. The recommendation engine analyzes features such as genres, keywords, cast, crew, and movie overview to generate personalized movie suggestions.

The project follows a complete Machine Learning workflow including:

- Data Collection
- Data Preprocessing
- Feature Engineering
- Vectorization
- Similarity Calculation
- Recommendation Generation
- Streamlit Web Application Development

---

## 📂 Dataset

The dataset was obtained from Kaggle and consists of:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

Dataset Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## ⚙️ Project Workflow

### 1. Data Collection
Imported the TMDB Movies and Credits datasets.

### 2. Data Preprocessing
- Merged movie and credit datasets
- Removed unnecessary columns
- Handled missing values
- Extracted important features

### 3. Feature Engineering
Created tags by combining:
- Genres
- Keywords
- Cast
- Crew (Director)
- Movie Overview

### 4. Text Processing
- Converted text to lowercase
- Removed spaces and special characters
- Applied text cleaning techniques

### 5. Vectorization
Used CountVectorizer from Scikit-Learn to convert textual movie information into numerical vectors.

### 6. Similarity Calculation
Calculated cosine similarity between movie vectors to identify movies with similar content.

### 7. Recommendation Engine
Developed a recommendation function that:
- Takes a movie title as input
- Finds the movie index
- Retrieves similarity scores
- Returns Top 5 most similar movies

### 8. Streamlit Web Application
Built an interactive web interface where users can:
- Select a movie
- Click the Recommend button
- View top recommended movies instantly

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Pickle
- Streamlit
- Jupyter Notebook

---

## 🚀 Features

✅ Content-Based Movie Recommendation

✅ Cosine Similarity Matching

✅ Interactive Streamlit Interface

✅ Fast Recommendation Generation

✅ User-Friendly Movie Selection

---

## 📸 Application Preview

Input Movie:
Avatar

Recommendations:
- Aliens vs Predator: Requiem
- Aliens
- Falcon Rising
- Independence Day
- Titan A.E.

---

## 📁 Project Structure

```text
Movie-Recommender-System/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── movie_recommender.ipynb
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/devank1234/movie_recommender_system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Movie Poster Integration using TMDB API
- Genre-Based Filtering
- Hybrid Recommendation System
- Collaborative Filtering
- User Ratings and Reviews
- Personalized Recommendations

---

## 👨‍💻 Author

**Devank Verma**

Dual Degree Student, Ceramic Engineering  
National Institute of Technology Rourkela

Aspiring Data Analyst | Machine Learning Enthusiast | MBA Aspirant
