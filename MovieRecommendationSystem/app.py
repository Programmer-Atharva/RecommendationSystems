
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e3ce9287688045e96e95c6c6db974e8f&language=en-US'.format(movie_id))

    data= response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies=[]
    recommended_posters=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_posters
movie_dict=pickle.load(open('movie_dict.pkl','rb'))

movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')
selected_movie_name=st.selectbox(
    "Choose a Movie similar to your Genre...",movies['title'].values)
if st.button('Recommend'):
    name,poster=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])