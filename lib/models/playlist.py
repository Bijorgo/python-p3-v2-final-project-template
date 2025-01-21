from models.__init__ import CURSOR, CONN

class Playlist:
    all_playlists = {}
    # ADD CODE TO OPERATIONS THAT MODIFY TABLES TO CHECK DICTIONARY AS WELL
    def __init__(self, name, description):
        self.id = None  # id will be set in database
        self._name = name
        self._description = description

    def __repr__(self):
        """Return a string representation of the playlist for debugging."""
        return f"Playlist(id={self.id}, name={self.name}, description={self.description})"

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
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a string of 1 or more characters")
        self._name = name

    @description.setter
    def description(self, description):
        if not isinstance(description, str) or not ( 0 <= len(description) <= 50):
            raise ValueError("Description must be a string between 0 and 50 characters")
        self._description = description

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
        print("All playlists have been deleted.")

    @classmethod
    def create(cls, name: str, description: str):
        """Initialize a new Playlist instance and save to the database"""
        # Check if playlist with that name exists
        sql = """
            SELECT 1
            FROM playlists
            WHERE name = ?
        """
        result = CURSOR.execute(sql, (name,)).fetchone()
        if not result:
            # If no result, create a new instance
            playlist = cls(name, description)
            playlist.save()
            print(f"Success! {playlist} created.")
            return playlist
        else:
            print("A playlist by that name already exists. Duplicate playlist not created.")

    @classmethod
    # MAY HAVE ISSUES, OVERRIDES Playlist INSTANCE IN ALL_PLAYLISTS WHEN CALLED, EVEN IF ROW ALREADY EXISTS IN DICTIONARY
    def instance_from_db(cls, row):
        """Return a Playlist object with attribute values from table row"""
        # Look up playlist by id in all_playlists dictionary
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
    def find_by_name(cls, name: str):
        """Return a Playlist object corresponding to the first table row matching given name"""
        sql = """
            SELECT *
            FROM playlists
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        print(f"Looking for playlist: {name}") # debugging
        print(f"Query result: {row}") # debugging
         
        if row:
           return Playlist.instance_from_db(row) 
        else:
            print("Playlist not found.")
    
    @classmethod 
    def find_by_id(cls, id):
        """Return a Playlist object corresponding to the first table row matching given id"""
        try:
            # Ensure the id is an integer
            id = int(id)  # Convert id to an integer if it's not already
        except ValueError:
            print(f"Error: Invalid id '{id}'")
            return None
        
        print(f"Looking for playlist with ID: {id}") # debugging to verify id
        
        sql = """
            SELECT *
            FROM playlists
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        print(f"Query result: {row}") # debugging
        return Playlist.instance_from_db(row) if row else None

    # Instance methods
    def save(self):
        """Insert a new row with the values of the current instance into playlists."""
        sql = """
            INSERT INTO playlists (name, description)
            VALUES (?, ?)
        """
        CURSOR.execute(sql,(self.name, self.description))
        CONN.commit()
        #Update object id attribute using primary key value of the new row.
        self.id = CURSOR.lastrowid
        #Save the object to all_playlists dictionary using the row's primary key as the dictionary key.
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
        """Delete the table row corresponding to the current Playlist instance."""
        sql = """
            DELETE FROM playlists
            WHERE id = ?
        """

        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        
        # Delete dictionary entry by id
        del type(self).all_playlists[self.id]
        # Set id to None
        self.id = None

    @classmethod
    def get_all(cls):
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
            FROM songs
            WHERE playlist_id = ?
        """
        CURSOR.execute(sql,(self.id,))
        rows = CURSOR.fetchall()
        return [Song.instance_from_db(row) for row in rows]

    #@classmethod
    #def add_song():
        #from song import Song
        #pass

    #@classmethod
    #def remove_song():
        #from song import Song
        #pass