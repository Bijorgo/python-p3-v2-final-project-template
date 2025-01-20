# lib/junction_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def adding_song_to_playlist():
    Junction.create_table() # Check if table exist, if no: create table
    # Input playlist
    playlist_entered = input("Enter playlist id: ")
    playlist_found = Playlist.find_by_id(playlist_entered)
    #print(f"Query result: {playlist_found}") #debugging

    # Input song
    song_entered = input("Enter song id: ")
    song_found = Song.find_by_id(song_entered)
    #print(f"Query result: {song_found}") #debugging
    
    # Try adding song playlist relationship
    if playlist_found and song_found:
            try:
                Junction.add_song_to_playlist(playlist_found.id, song_found.id)
                print(f"Sucess! {song_found.title} added to {playlist_found.name}!")
            except Exception as exc:
                print(f"Error adding {song_found} to {playlist_found}.", exc)
    else:
        print(f"Sorry, playlist `{playlist_entered}` or `{song_found} not found.")

def clear_all_relationships():
     Junction.drop_table()
     print(f"All playlists cleared.")