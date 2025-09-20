from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2 import connect
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('USER')
PASS = os.getenv('PASS')
DB = os.getenv('DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'Artist'
    ArtistId = Column(Integer, primary_key=True, index = True)
    Name = Column(String)

class Album(Base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True, index = True)
    Title = Column(String)
    ArtistId = Column(Integer)

class Track(Base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(Integer)
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Byte = Column(Integer)
    UnitPrice = Column(Integer)

class Customer(Base):
    __tablename__ = 'Customer'
    CustomerId = Column(Integer, primary_key=True, index=True)
    

DATABASE_URL = f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}'