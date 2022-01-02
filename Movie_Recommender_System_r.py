from re import I
import streamlit as st
import pickle
import pandas as pd
import requests
from itertools import cycle


hide_menu_style = """
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            </style>
            """
st.markdown(hide_menu_style, unsafe_allow_html=True)
def fetch_poster(movie_id):
    url ='https://api.themoviedb.org/3/movie/{}?api_key=8d4222eaf0fc55d4781fe3e4f2650478&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    
    return recommended_movie_names,recommended_movie_posters

movies_list = pickle.load(open('movies.pkl','rb'))
movies= pd.DataFrame(movies_list)
movies_list =movies_list['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie =st.selectbox('Search for Movies here:',movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    cols =cycle(st.columns((1,1,1)))
    for idx, recommended_movie_poster in enumerate(recommended_movie_posters):
        next(cols).image(recommended_movie_poster, caption=recommended_movie_names[idx])