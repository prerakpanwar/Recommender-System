import pandas as pd
import streamlit as st
import pickle
import requests

def get_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=30849ed424ec72604fb44e1aae42e4d9&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]     #df name is movies here
    distances = result[movie_index]
    list_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in list_movies:
        movieID = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # get poster using API
        recommended_posters.append(get_poster(movieID))
    return recommended_movies,recommended_posters


movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

result = pickle.load(open('similarity_matrix.pkl', 'rb'))

st.title('The Movie Recommender System')

selected_movie = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i % 5]:  # Looping through the columns cyclically
            st.text(names[i])
            st.image(posters[i])


# if st.button('Recommend'):
#     names, posters = recommend(selected_movie)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])


