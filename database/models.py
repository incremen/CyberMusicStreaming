# models.py
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    playlists = relationship('Playlist', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"


class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)

    user = relationship('User', back_populates='playlists')
    songs = relationship('Song', back_populates='playlist')

    def __repr__(self):
        return f"<Playlist(id={self.id}, , user_id={self.user_id})>"


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    length = Column(Float)
    nframes = Column(Integer)
    framerate = Column(Integer)
    nchannels = Column(Integer)
    playlist_id = Column(Integer, ForeignKey('playlists.id'))

    playlist = relationship('Playlist', back_populates='songs')

    def __repr__(self):
        return f"""<Song(id={self.id}, name={self.name}, length={self.length}, 
    nframes={self.nframes}, framerate={self.framerate}, nchannels={self.nchannels}, playlist_id={self.playlist_id})>"""
