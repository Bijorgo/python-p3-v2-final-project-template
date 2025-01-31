# lib/models/junction.py

from models.__init__ import CURSOR, CONN

class Junction:
    def __init__(self, playlist, song):
        self.playlist = playlist
        self.song = song

    @classmethod
    def create_table(cls):
        """Creates junctions table if it doesn't already exist"""
        sql = """
            CREATE TABLE IF NOT EXISTS junctions(
                id INTEGER PRIMARY KEY,
                playlist_id INEGER,
                song_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES playlists(id),
                FOREIGN KEY (song_id) REFERENCES songs(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Deletes junction table"""
        sql = """
            DROP TABLE IF EXISTS junctions
        """
        CURSOR.execute(sql)
        CONN.commit()
        print(f"All playlists cleared.")

    @classmethod
    def add_song_to_playlist(cls, playlist_id, song_id):
        """Add a song to a playlist in junctions table"""
        sql = """
            SELECT 1
            FROM junctions
            WHERE playlist_id = ?
            AND song_id = ?
        """
        result = CURSOR.execute(sql,(playlist_id, song_id,)).fetchone()
        if not result:
            junction = cls(playlist_id, song_id)
            junction.save()
            print(f"Sucess! Song added to playlist.")
            return junction
        else:
            print("Song already exists in playlist")

    @classmethod
    def remove_song_from_playlist(self, playlist_id, song_id):
        """Delete a song from a playlist in junctions table"""
        sql = """
            DELETE FROM junctions
            WHERE playlist_id = ?
            AND song_id = ?
        """
        CURSOR.execute(sql,(playlist_id, song_id,))
        CONN.commit()
        print(f"Sucess! Song removed from playlist.")

    @classmethod
    def view_songs_in_playlist(self, playlist_id):
        """Retrieves all songs in a specific playlist by joining the Junction and Songs tables"""
        # Shuffle function would go here
        sql = """
            SELECT songs.id, songs.title, songs.artist, songs.genre, songs.duration
            FROM songs
            JOIN junctions ON songs.id = junctions.song_id
            WHERE junctions.playlist_id = ?
        """
        songs = CURSOR.execute(sql,(playlist_id,)).fetchall()
        if songs:
            return songs
        else:
            print("No songs in playlist.")
            return None
    
    def save(self):
        """Insert a new row with the values of the current instance into junctions table"""
        sql = """
            INSERT INTO junctions(playlist_id, song_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.playlist, self.song))
        CONN.commit()
