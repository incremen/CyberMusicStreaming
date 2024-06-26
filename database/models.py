# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_playlist_association = Table(
    'user_playlist_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('playlist_id', Integer, ForeignKey('playlists.id'))
)

song_playlist_association = Table(
    'song_playlist_association',
    Base.metadata,
    Column('song_id', Integer, ForeignKey('songs.id')),
    Column('playlist_id', Integer, ForeignKey('playlists.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    playlists = relationship(
        'Playlist',
        secondary=user_playlist_association,
        back_populates='users',
        lazy='subquery'
    )

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, password={self.password})"
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    users = relationship(
        'User',
        secondary=user_playlist_association,
        back_populates='playlists'
    )
    songs = relationship(
        'Song',
        secondary=song_playlist_association,
        back_populates='playlists',
        lazy='subquery'
    )
    def __repr__(self):
        return f"Playlist(name={self.name}, id={self.id})"
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    length = Column(Float)
    nframes = Column(Integer)
    framerate = Column(Integer)
    nchannels = Column(Integer)

    playlists = relationship(
        'Playlist',
        secondary=song_playlist_association,
        back_populates='songs'
    )
    
    def as_dict(self):
        """
        Return a dictionary representation of the object, with keys as column names and values as attribute values.
        """
        song_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return song_dict
    
    def __repr__(self):
        return f"Song(name={self.name})"
