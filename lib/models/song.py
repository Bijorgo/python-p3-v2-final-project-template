class Song:
    def __init__(self, title, artist, genre, duration):
        self._title = title
        self._artist = artist
        self._genre = genre
        self._duration = duration

    @property
    def title(self):
        return self._title
    
    @property
    def artist(self):
        return self._artist
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def duration(self):
        return self._duration
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        self._title = title

    @artist.setter
    def artist(self, artist):
        if not isinstance(artist, str):
            raise ValueError("Artist must be a string")
        
    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, str):
            raise ValueError("Genre must be a string")
        
    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise ValueError("Duration must be a decimal number")