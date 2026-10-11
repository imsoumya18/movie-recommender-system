import os
import streamlit as st
import pickle
import requests

TMDB_API_KEY = os.environ.get("TMDB_API_KEY") or st.secrets.get("TMDB_API_KEY", "")
PLACEHOLDER_POSTER = "https://via.placeholder.com/500x750?text=No+Poster"

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}",
            params={"api_key": TMDB_API_KEY},
            timeout=10,
        )
        response.raise_for_status()
        poster_path = response.json().get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except requests.RequestException:
        pass
    return PLACEHOLDER_POSTER

def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    recommended_movies = []
    recommended_posters = []
    for idx in neighbors[movie_idx]:
        row = movies.iloc[idx]
        recommended_movies.append(row.title)
        recommended_posters.append(fetch_poster(row.movie_id))

    return recommended_movies, recommended_posters

neighbors = pickle.load(open('neighbors.pkl', 'rb'))
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

st.title('Movie Recommendation System')

seleced_movie = st.selectbox("Enter movie name", movies_list,index=None, placeholder="")

if st.button("Recommend") and seleced_movie:
    names, posters = recommend(seleced_movie)
    for col, name, poster in zip(st.columns(5), names, posters):
        with col:
            st.image(poster)
            st.caption(name)
