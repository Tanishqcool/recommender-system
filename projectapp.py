import streamlit as st
import pickle
import pandas as pd


new_dict = pickle.load(open('movies.pkl', 'rb'))
new = pd.DataFrame(new_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    movies = []
    for i in movie_list:
        movies.append(new.iloc[i[0]].title)
    return movies


st.title('Movie Recommender System')
selected_movie = st.selectbox('I will recommend you 5 movies .', new['title'].values)
if st.button('Recommend'):
    recommended_movies = recommend(selected_movie)
    for i in recommended_movies:
     st.write(i)

