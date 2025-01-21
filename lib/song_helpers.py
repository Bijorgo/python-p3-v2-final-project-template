# lib/song_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def create_new_song():
    Song.create_table() # Check if table exist, if no: create table
    title = input("Ener song title: ")
    artist = input("Enter artist name: ")
    genre = input("Enter genre: ")
    duration = input("Enter duration: ")
    try:
        Song.create(title, artist, genre, duration)
    except Exception as exc:
        print("Error creating song: ", exc)

def delete_song():
    Song.create_table()
    id = input("Enter song id: ")
    song = Song.find_by_id(id)
    if song:
        song.delete()
        print(f"Song {song} deleted.")
    else:
        print(f"Song {song} not found")

def display_all_songs():
    Song.create_table()
    songs = Song.get_all()
    if songs:
        for song in songs:
            print(song)
    else:
        print("No songs to display.")

def find_song_by_title():
    Song.create_table()
    song_entered = input("Enter song title: ")
    song = Song.find_by_title(song_entered)
    if song:
        print(song)
    else:
        print(f"Sorry, {song} not found")

def update_song_info():
    pass