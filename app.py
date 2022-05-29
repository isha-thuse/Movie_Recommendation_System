import pickle
import streamlit as st
import requests
import pandas as pd
from PIL import Image

# impoertin
img=Image.open('Movies.jpg')
st.image(img)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    recommended_movie_names = []
   # recommended_movie_posters = []
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    for i in movies_list:
        # fetch the movie poster
        # movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


movies_dict = pickle.load(open('movies_RS_dict.pkl','rb'))

movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.header('Movie Recommender System')
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i in range(5):
        st.write(recommended_movie_names[i])

