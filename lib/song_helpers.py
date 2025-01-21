# lib/song_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def find_song():
    Song.create_table()
    given_title = input("Enter song title: ").strip().lower()
    given_artist = input("Enter artist name: ").strip().lower()
    song = Song.find_one_song(given_title, given_artist)
    return song, given_title, given_artist

def create_new_song():
    Song.create_table() # Check if table exist, if no: create table
    title = input("Ener song title: ").strip().lower()
    artist = input("Enter artist name: ").strip().lower()
    genre = input("Enter genre: ").strip().lower()
    duration = input("Enter duration: ").strip().lower()
    try:
        Song.create(title, artist, genre, duration)
    except Exception as exc:
        print("Error creating song: ", exc)

def delete_song():
    song, given_title, given_artist = find_song()
    if song:
        song.delete()
        print(f"Sucess! Song {song.title} deleted.")
    else:
        print(f"Song {given_title} by {given_artist} not found")

def display_all_songs():
    Song.create_table()
    songs = Song.get_all()
    if songs:
        for song in songs:
            print(song)
    else:
        print("No songs to display.")

def find_song_by_title():
    song, given_title = find_song()
    if song:
        print(f"Song found!")
        print(f"Title: {song.title}, Artist: {song.artist}, Genre: {song.genre}, Duration: {song.duration}")
    else:
        print(f"Sorry, {given_title} not found")

def update_song_info():
    pass