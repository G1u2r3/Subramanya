# Subramanya
# Movie Recommendation API

Welcome to the Movie Recommendation API! This project provides a RESTful API for managing movies and user ratings, along with a movie recommendation feature based on user input.

## Features

- **Create Movies**: Add new movies to the database.
- **Get Movies**: Retrieve a list of all movies or get details of a specific movie by ID.
- **Create Ratings**: Submit user ratings for movies.
- **Get Recommendations**: Fetch movie recommendations based on a specific movie title.

## Technologies Used

- **FastAPI**: For building the API.
- **SQLAlchemy**: For database interaction.
- **SQLite**: For storing movie and rating data.
- **Pydantic**: For data validation.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd movie-recommendation-api

## API Endpoints

- **GET /**: Returns a welcome message for the API.
- **POST /movies/**: Creates a new movie.
- **GET /movies/**: Retrieves a list of all movies.
- **GET /movies/{movie_id}**: Retrieves a specific movie by its ID.
- **POST /ratings/**: Creates a new rating for a movie.
- **GET /recommendations/{movie_title}**: Fetches movie recommendations based on a specific title.



