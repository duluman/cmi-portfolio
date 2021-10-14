import sqlalchemy as db
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.schema import Column

engine = db.create_engine('sqlite:////Users/luchicla/Downloads/Chinook_Sqlite.sqlite')
connection = engine.connect()

artist = db.Table('Artist', db.MetaData(), autoload_with=engine)
print(artist.columns.keys())

query = db.select([artist])
rr = connection.execute(query)
r = rr.fetchall()
# print(r)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
Base.metadata.bind = engine

session = Session(engine)


class Artist(Base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)

class Album(Base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String)
    ArtistId = Column(Integer)

artist = Artist()
artist.Name = "sample sqlalchemy"
print(artist)

session.add(artist)
session.commit()

r = session.query(Artist)
import sys 
print(sys.getsizeof(list(r)))
