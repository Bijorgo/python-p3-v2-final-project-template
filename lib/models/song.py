from models.__init__ import CURSOR, CONN

class Song:
    all_songs = {}

    def __init__(self, title, artist, genre, duration=None):
        self.id = None # id assignment will happen in database
        self._title = title
        self._artist = artist
        self._genre = genre
        self._duration = duration

    def __repr__(self):
        """Return a string representation of the playlist"""
        return f"Song(id={self.id}, title = {self.title}, artist = {self.artist}, genre = {self.genre}, diration = {self.duration})"

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
        if not isinstance(title, str) or len(title) == 0: # Validation data type, length
            raise ValueError("Title must be a string of one or more characters")
        self._title = title

    @artist.setter
    def artist(self, artist):
        if not isinstance(artist, str) or len(artist) == 0: # Validation data type, length
            raise ValueError("Artist must be a string one or more characters")
        self._artist = artist
        
    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, str) or len(genre) == 0: # Validation data type, length
            raise ValueError("Genre must be a string one or more characters")
        self._genre = genre
        
    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (float, int)): # Validation data type
            raise ValueError("Duration must be a decimal number")
        self._duration = duration
        
    # Class methods
    @classmethod
    def create_table(cls):
        """Create a new table that persists the attibutes of Song instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY,
            title TEXT,
            artist TEXT,
            genre TEXT,
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
        Song.all_songs.clear() # clear dictionary
        print("All songs have been deleted")
           
    @classmethod   
    def create(cls, title: str, artist: str, genre: str, duration: float):
        """Inititalize a new Song instance and save to database""" 
        # Check if song with that title and artist combo exist
        sql = """
            SELECT 1 
            FROM songs
            WHERE title = ?
            AND artist = ?
        """
        result = CURSOR.execute(sql, (title, artist,)).fetchone()
        # Create new Song instance if not already existing 
        if not result: 
            song = cls(title, artist, genre, duration)
            song.save()
            print(f"Sucess! {song.title} created.")
            return song
        else:
            print("A song by that title and artist already exists.")

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
        # Return as a list
        return [Song.instance_from_db(row) for row in rows]

    @classmethod
    def find_one_song(cls, title, artist):
        """Return a Song object correspnding to the first row matching the given title"""
        sql = """
            SELECT *
            FROM songs
            WHERE title = ?
            AND artist = ?
        """
        row = CURSOR.execute(sql, (title, artist,)).fetchone()
        #print(f"Looking for song titled: {title}") # debugging
        #print(f"By artist: {artist}") # debugging
        #print(f"Query result: {row}") # debugging
        if row:
           return Song.instance_from_db(row) 
        else:
            print("Song not found.")
            return None

    # Instance methods
    def save(self):
        """Insert a new row with the values of the current instance into songs."""
        sql = """
            INSERT INTO songs(title, artist, genre, duration)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.artist, self.genre, self.duration))
        CONN.commit()
        # Update object id atribute using primary key value of the new row.
        self.id = CURSOR.lastrowid
        # Save the bject to all_songs dictionary using the row's primary key as the dictionary key
        Song.all_songs[self.id] = self

    def update(self):
        """Update table row corresponding to current Song instance"""
        sql = """
            UPDATE songs
            SET title = ?, artist = ?, genre = ?, duration = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.artist, self.genre, self.duration, self.id,))
        CONN.commit()
        # Update dictionary
        type(self).all_songs[self.id] = self
        print(f"Sucess! Song updated: Title: {self.title}, Artist: {self.artist}, Genre: {self.genre}, Duration: {self.duration}")

    def delete(self):
        """Delete the row corresponding to the current Song instance,
        delete dictionary entry, and ressaign id attribute.""" 
        sql = """
            DELETE FROM songs
            WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        # Delete dictionary entry by id
        del type(self).all_songs[self.id]
        # Set id to None
        self.id = None
        print(f"Sucess! Song {self.title} deleted.")