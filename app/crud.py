from sqlalchemy.orm import Session
from app import models, schemas

# Create a new movie
def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(title=movie.title, genre=movie.genre, year=movie.year, rating=movie.rating)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# Get a movie by ID
def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

# Get all movies
def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

# Add a rating
def create_rating(db: Session, rating: schemas.RatingCreate):
    db_rating = models.Rating(user_id=rating.user_id, movie_id=rating.movie_id, rating=rating.rating)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
