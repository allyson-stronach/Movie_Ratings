from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

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

    #User table is backreferenced from Rating table

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    # we don't need the line below! in this table, there will only be one movie--remake db???
    #movie_id = Column(Integer, nullable=True)
    name = Column(String (64), nullable=True)
    released_at = Column(DateTime, nullable=True)
    imdb_url = Column(String (200), nullable=True)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=True)
    rating = Column(Integer, nullable=True)
    timestamp = Column(DateTime, nullable=True)

    user = relationship("User", backref=backref("ratings", order_by=id))
    #added the line below to access movie name from ratings table; not sure about the order_by=id part...see above for id issue
    movie = relationship("Movie", backref=backref("ratings", order_by=id))


### End class declarations


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
