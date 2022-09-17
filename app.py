import streamlit as st
import pickle
import pandas as pd

def rec(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

    reced = []
    for i in movies_list:
        reced.append(movies.iloc[i[0]].title)
    return reced
movies_d = pickle.load(open('moviesrecdict.pkl', 'rb'))
movies = pd.DataFrame(movies_d)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recs')
movie_option = st.selectbox(
    'Tell me your favorite movie and get amazing recommendations for your next watch!',
    movies['title'].values
)

if st.button('Recommend me my next watch!'):
    recommended = rec(movie_option)
    for i in recommended:
        st.write(i)



