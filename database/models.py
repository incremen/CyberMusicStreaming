# models.py
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
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
    items = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='playlists')

    def __repr__(self):
        return f"<Playlist(id={self.id}, items={self.items}, user_id={self.user_id})>"
    
    def get_as_list(self):
        return eval(self.items)
