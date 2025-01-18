from __init__ import CURSOR, CONN

class Playlist:
    all_playlists = {}
    def __init__(self, name, description):
        self.id = None  # id will be set in database
        self._name = name
        self._description = description

    # All proprty attributes
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    # All property setters
    @name.setter
    def name(self, name):
        if not isinstance(name, str) and len(name) > 0:
            raise ValueError("Name must be a string of 1 or more characters")
        self._name = name

    @description.setter
    def description(self, description):
        if not isinstance(description, str) and ( 0 <= len(description) <= 50):
            raise ValueError("Description must be a string between 0 and 50 characters")
    
    # Class methods
    @classmethod
    def create_table(cls):
        """Create a new table that persists the attributes of Playlist instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS playlists(
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Playlist instances """
        sql = """
            DROP TABLE IF EXISTS playlists;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, description):
        """Initialize a new Playlist instance and save to the database"""
        playlist = cls(name, description)
        playlist.save()

    @classmethod
    def instance_from_db(cls, row):
        """Docstring"""
        playlist = cls.all_playlists.get(row[0])
        if playlist:
            playlist.name = row[1]
            playlist.description = row[2]
        else:
            playlist = cls(row[1], row[2])
            playlist.id = row[0]
            Playlist.all_playlists[playlist.id] = playlist
        return playlist
    
    @classmethod 
    def find_by_name(cls, name):
        """Return a Playlist object corresponding to the first table row matching given name"""
        sql = """
            SELECT *
            FROM playlists
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return Playlist.instance_from_db(row) if row else None

    # Instance methods
    def save(self):
        """Insert a new row with the values of the current instance into playlists. 
        Update object id attribute using primary key value of the new row.
        Save the object to all_playlists dictionart using the row' primary key as the dictionary key."""
        sql = """
            INSERT INTO playlists (name, description)
            VALUES (?, ?)
        """
        CURSOR.execute(sql)
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all_playlists[self.id] = self

    def update(self):
        """Update table row corresponding to current Playlist instance"""
        sql = """
            UPDATE playlists
            SET name = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description, self.id,))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Playlist instance,
        delete dictionary entry, and reassign id attribute
        """
        sql = """
            DELETE FROM playlists
            WHERE id = ?
        """

        CURSOR.execute(self,(self.id,))
        CONN.commit()
        
        # Delete dictionary entry by id
        del type(self).all_playlists[self.id]
        # Set id to None
        self.id = None

    @classmethod
    def get_all():
        """Return a list containing a Playlist object per row in the table"""
        sql = """
            SELECT *
            FROM playlists
        """

        rows = CURSOR.execute(sql).fetchall()
        return [Playlist.instance_from_db(row) for row in rows]

    def view_songs(self):
        """Return a list of songs associated with current playlist"""
        from song import Song    
        sql = """
            SELECT *
            WHERE playlist_id = ?
        """
        CURSOR.execute(sql,(self.id,))

        rows = CURSOR.fetchall()
        return [Playlist.instance_from_db(row) for row in rows]

    @classmethod
    def add_song():
        pass

    @classmethod
    def remove_song():
        pass