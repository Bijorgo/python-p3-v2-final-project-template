from models.__init__ import CURSOR, CONN

class Song:
    all_songs = {}

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
    @classmethod
    def create_table(cls):
        """Create a new table that persists the attibutes of Song instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY
            title TEXT
            artist TEXT
            genre TEXT 
            duration REAL
            )"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Delete the table that persists Song instances"""
        sql = """
            DROP TABLE IF EXISTS songs
        """
        CURSOR.execute(sql)
        CONN.commit()
           
    @classmethod   
    def create(cls, title, artist, genre, duration):
        """Inititalize a new Song instance and save to database""" 
        song = cls(title, artist, genre, duration)
        song.save()

    @classmethod
    def instance_from_db(cls, row):
        """Return a Song object with attribute values from table row"""
        song = cls.all_songs.get(row[0])
        if song:
            song.title = row[1]
            song.artist = row[2]
            song.genre = row[3]
            song.duration = row[4]
        else:
            song = cls(row[1], row[2], row[3], row[4])
            song.id = row[0]
            Song.all_songs[song.id] = song
        return song
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Song object per row in the table""" 
        sql = """
            SELECT *
            FROM songs
        """

        rows = CURSOR.execute(sql).fetchall()
        return [Song.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_title(cls, title):
        """Return a Song object correspnding to the first row matching the given title"""
        sql = """
            SELECT *
            FROM songs
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return Song.instance_from_db(row) if row else None

    #@classmethod
    #def find_by_artist(cls, artist):
        #"""Return a list of Song objects corresspondng to a given artist"""

    # Instance methods
    def save(self):
        """Insert a new row with the values of the current instance into songs.
        Update object id atribute using primary key value of the new row.
        Save the bject to all_songs dictionary using the row's primary key as the dictionary key"""
        sql = """
            INSERT INTO songs
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql)
        CONN.commit()

    def delete(self):
        """Delete the row corresponding to the current Song instance,
        delete dictionary entry, and ressaign id attribute.""" 
        sql = """
            DELETE FROM songs
            WHERE id = ?"""
        CURSOR.execute(sql)
        CONN.commit()

        # Delete dictionary entry by id
        del type(self).all_songs[self.id]
        # Set id to None
        self.id = None