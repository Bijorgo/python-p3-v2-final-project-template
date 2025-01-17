class Song:
    def __init__(self, title, artist, genre, duration=None):
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
        if not isinstance(title, str) and len(title) > 0:
            raise ValueError("Title must be a string of one or more characters")
        self._title = title

    @artist.setter
    def artist(self, artist):
        if not isinstance(artist, str) and len(artist) > 0:
            raise ValueError("Artist must be a string one or more characters")
        
    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, str) and len(genre) > 0:
            raise ValueError("Genre must be a string one or more characters")
        
    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise ValueError("Duration must be a decimal number")