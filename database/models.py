# models.py
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
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

    # Use the association table for the many-to-many relationship
    playlists = relationship(
        'Playlist',
        secondary=user_playlist_association,
        back_populates='users'
    )

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Use the association table for the many-to-many relationship
    users = relationship(
        'User',
        secondary=user_playlist_association,
        back_populates='playlists'
    )
    songs = relationship(
        'Song',
        secondary=song_playlist_association,
        back_populates='playlists'
    )
    def __repr__(self):
        return f"Playlist(name={self.name}, id={self.id})"


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    length = Column(Float)
    nframes = Column(Integer)
    framerate = Column(Integer)
    nchannels = Column(Integer)
    playlist_id = Column(Integer, ForeignKey('playlists.id'))

    playlists = relationship(
        'Playlist',
        secondary=song_playlist_association,
        back_populates='songs'
    )
    
    def as_dict(self):
        """
        Return a dictionary representation of the object, with keys as column names and values as attribute values.
        Doesn't include id or playlist id
        """
        song_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        del song_dict['id']
        del song_dict['playlist_id']
        return song_dict
    
    def __repr__(self):
        return f"Song(id={self.id}, name={self.name}, length={self.length}, \
nframes={self.nframes}, framerate={self.framerate}, nchannels={self.nchannels}, playlist_id={self.playlist_id})"
