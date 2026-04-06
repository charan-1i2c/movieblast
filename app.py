import os
import pickle
import streamlit as st
from PIL import Image

# Load models and data
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Function to fetch poster path safely
def fetch_poster(movie_title):
    # Sanitize title to create filename
    safe_title = movie_title.translate(str.maketrans('', '', r'\/:*?"<>|')).strip()
    filename = f"{safe_title}.jpg"
    path = os.path.join("posters", filename)

    if os.path.exists(path):
        return path
    else:
        return os.path.join("posters", "default.jpg")

# Recommendation logic
def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = similarity[idx]
    # Sort by similarity score, get top 5 excluding the first (itself)
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    names = []
    posters = []
    for i in movie_indices:
        title = movies.iloc[i[0]].title
        names.append(title)
        posters.append(fetch_poster(title))
    return names, posters

# UI setup
st.set_page_config(page_title="MovieMatch", page_icon="🎬", layout="wide")
st.title('🎬 Movie Recommender (Offline Version)')

# Movie selection
selected_movie = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Show recommendations
if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie)
    
    # Use columns for a cleaner grid layout
    cols = st.columns(5)
    
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.markdown(f"**{name}**")
            img = Image.open(poster)
            st.image(img, use_container_width=True)
