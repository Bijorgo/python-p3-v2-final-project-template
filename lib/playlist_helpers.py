# lib/playlist_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def create_new_playlist():
    Playlist.create_table() # Check if table exist, if no: create table
    name = input("Enter playlist name: ")
    description = input("Enter playlist description: ")
    try:
        playlist = Playlist.create(name, description) # Create new playlist instance
        print(f"Success! {playlist} created.")
    except Exception as exc:
        print("Error creating playlist: ", exc)

def delete_playlist():
    id = input("Enter playlist id: ")
    playlist = Playlist.find_by_id(id)
    if playlist:
        playlist.delete()
        print(f"Playlist {playlist} deleted.")
    else:
        print(f"Playlist {playlist} not found.")

def display_all_playlists():
    playlists = Playlist.get_all()
    if playlists:
        for playlist in playlists:
            print(playlist)
    else: 
        print("No playlists to display.")

def find_playlist_by_name():
    name = input("Enter playlist name: ")
    playlist = Playlist.find_by_name(name)
    if playlist:
        print(playlist)
    else:
        print(f"Sorry, {playlist} not found.")


def exit_program():
    print("Goodbye!")
    exit()
