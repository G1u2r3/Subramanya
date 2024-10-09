from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.ml_model import get_movie_recommendations


# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}

# Route to create a new movie
@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db=db, movie=movie)

# Route to get all movies
@app.get("/movies/", response_model=list[schemas.Movie])
def get_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip=skip, limit=limit)

# Route to get a movie by ID
@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

# Route to create a rating
@app.post("/ratings/", response_model=schemas.Rating)
def create_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    return crud.create_rating(db=db, rating=rating)


# Route to get movie recommendations
@app.get("/recommendations/{movie_title}")
def get_recommendations(movie_title: str, db: Session = Depends(get_db)):
    recommendations = get_movie_recommendations(movie_title)
    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"movie_title": movie_title, "recommendations": recommendations}
