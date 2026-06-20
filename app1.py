# Generated from: app1.ipynb
# Converted at: 2026-06-20T07:47:23.164Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import  streamlit as st
import pandas as pd
import pickle


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


from streamlit import selectbox

st.title("Movie Recommender System")

selected_movie_name=selectbox(
"Enter Movie name",
movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      st.write(i)