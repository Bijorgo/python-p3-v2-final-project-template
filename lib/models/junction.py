from __init__ import CURSOR, CONN

class Junction:
    def __init__(self, playlist, song):
        self.playlist = playlist
        self.song = song

    @classmethod
    def create_table(cls):
        """Creates a junctions table if it doesn't already exist"""
        sql = """
            CREATE TABLE junctions(
            id PRIMARY KEY
            playlist_id FOREIGN KEY
            song_id FOREIGN KEY)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        pass

    def add_song_to_playlsit(self, playlist_id, song_id):
        pass

    def remove_song_from_playlist(self, playlist_id, song_id):
        pass

    def view_songs_in_playlist(self):
        """Retrieves all songs in a specific playlist by joining the Junction and Songs tables"""
        # Shuffle function would go here
        pass

    def get_songs_in_playlsit(playlist_id):
        """Retrieves all song IDs in a specific playlist"""
        # For advanced function(calculate duration), leave for later
        pass

    def find_by_playlist_id(self, playlist_id):
        """Retrieves all songs in a playlsit by playlist id"""
        # not sure about which class this should go in
        pass
