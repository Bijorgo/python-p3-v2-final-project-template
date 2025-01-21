# lib/playlist_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def create_new_playlist():
    Playlist.create_table() # Check if table exist, if no: create table
    name = input("Enter playlist name: ").strip().lower()
    description = input("Enter playlist description: ").strip().lower()
    try:
        Playlist.create(name, description) # Create new playlist instance
    except Exception as exc:
        print("Error creating playlist: ", exc)

def delete_playlist():
    Playlist.create_table()
    given_name = input("Enter playlist name: ").strip().lower()
    playlist = Playlist.find_by_name(given_name)
    if playlist:
        playlist.delete()
        print(f"Playlist {playlist} deleted.")
    else:
        print(f"Playlist {given_name} not found.")

def display_all_playlists():
    Playlist.create_table()
    playlists = Playlist.get_all()
    if playlists:
        for playlist in playlists:
            print(playlist)
    else: 
        print("No playlists to display.")

def find_playlist_by_name():
    Playlist.create_table()
    name = input("Enter playlist name: ").strip().lower()
    playlist = Playlist.find_by_name(name)
    if playlist:
        print(playlist)
    else:
        print(f"Sorry, playlist {playlist} not found.")

def update_playlist_info():
    pass