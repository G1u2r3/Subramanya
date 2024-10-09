import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load movie data from CSV (this will be loaded into the database in production)
movies = pd.read_csv('data/movies.csv')

# Content-based recommendation system using genres
def get_movie_recommendations(movie_title, num_recommendations=5):
    # Check if the movie exists in the dataset
    if movie_title not in movies['title'].values:
        return []
    
    # Vectorize the genres to compute similarity
    count_vectorizer = CountVectorizer(stop_words='english')
    genre_matrix = count_vectorizer.fit_transform(movies['genre'])

    # Compute cosine similarity between movies
    cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

    # Get index of the selected movie
    idx = movies.index[movies['title'] == movie_title][0]

    # Get similarity scores for all movies
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the most similar movies
    movie_indices = [i[0] for i in sim_scores[1:num_recommendations+1]]

    # Return the top N similar movies
    return movies['title'].iloc[movie_indices].tolist()
