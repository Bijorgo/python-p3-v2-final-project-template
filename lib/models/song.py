class Song:
    all_songs = []

    def __init__(self, title, artist, genre, duration=None):
        self.id = None # id assignment will happen in database
        self._title = title
        self._artist = artist
        self._genre = genre
        self._duration = duration
        Song.all_songs.append(self)

    # All attribute getters
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
    
    # All attribute setters
    @title.setter
    def title(self, title):
        if not isinstance(title, str) and len(title) > 0:
            raise ValueError("Title must be a string of one or more characters")
        self._title = title

    @artist.setter
    def artist(self, artist):
        if not isinstance(artist, str) and len(artist) > 0:
            raise ValueError("Artist must be a string one or more characters")
        self._artist = artist
        
    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, str) and len(genre) > 0:
            raise ValueError("Genre must be a string one or more characters")
        self._genre = genre
        
    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise ValueError("Duration must be a decimal number")
        self.duration = duration
        
    # Class methods
    #@classmethod
    #def add_to_all_songs(cls):
        #Song.all_songs.append() 
           
    @classmethod   
    def create(cls, title, artist, genre, duration):
        """Create new song in database""" 
        Song(title, artist, genre, duration)
        # consider preventing duplicate songs

    def delete(self, ):
        """Delete song in database by id""" 
        pass

    @classmethod
    def get_all(cls):
        """Retrieve all songs in database""" 
        pass

    @classmethod
    def find_by_attribute(cls, attribute, value):
        """Find song in database by title, artist, or genre""" 
        pass