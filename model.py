from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()
#each class below (User, Movie, Rating) is basically an instance of Base (a super class). The instructions said this was sort of "magical"

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    zip_code = Column(String(15), nullable=True)
    email = Column(String (64), nullable=True)
    password = Column(String(64), nullable=True)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    name = Column(String (64), nullable=True)
    released_at = Column(DateTime, nullable=True)
    imdb_url = Column(String, nullable=True)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, nullable = True)
    movie_id = Column(Integer, nullable=True)
    rating = Column(Integer, nullable=True)
    timestamp = Column(DateTime, nullable=True)


### End class declarations


def connect():
    global ENGINE
    global Session

    ENGINE =create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)
    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
