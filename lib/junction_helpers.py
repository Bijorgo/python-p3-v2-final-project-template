# lib/junction_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def add_song_to_playlist():
    Junction.create_table() # Check if table exist, if no: create table
    playlist_entered = input("Enter playlist id: ")
    song_entered = input("Enter song id: ")
    playlist_found = Playlist.find_by_id(playlist_entered)
    song_found = Song.find_by_id(song_entered)
    if playlist_found:
        print(f"Playlist {playlist_found} found.") #debugging
        if song_found:
            try:
                added_song = Junction.add_song_to_playlist(playlist_found, song_found)
                print(f"Sucess! {song_found} added to {playlist_found}!")
                print(f"{added_song}") # debugging
            except Exception as exc:
                print(f"Error adding {song_found} to {playlist_found}.", exc)
        else:
            print(f"Sorry, song `{song_entered}` not found.")
    else:
        print(f"Sorry, playlist `{playlist_entered}` not found.")