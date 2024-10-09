from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    genre: str
    year: int
    rating: float

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    user_id: int
    movie_id: int
    rating: float

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True
