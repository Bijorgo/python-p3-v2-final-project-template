# lib/junction_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def adding_song_to_playlist():
    Junction.create_table() # Check if table exist, if no: create table
    # Input playlist
    playlist_entered = input("Enter playlist name: ")
    playlist_found = Playlist.find_by_name(playlist_entered)
    #print(f"Query result: {playlist_found}") #debugging

    # Input song
    song_title_entered = input("Enter song title: ")
    song_artist_entered = input("Enter song artist: ")
    song_found = Song.find_one_song(song_title_entered, song_artist_entered)
    print(f"Query result: {song_found.title}") #debugging
    
    # Try adding song playlist relationship
    if playlist_found and song_found:
            try:
                Junction.add_song_to_playlist(playlist_found.id, song_found.id)
                print(f"Sucess! {song_found.title} added to {playlist_found.name}!")
            except Exception as exc:
                print(f"Error adding {song_found} to {playlist_found}.", exc)
    else:
        print(f"Sorry, playlist `{playlist_entered}` or `{song_found} not found.")

def remove_song_from_playlist():
    pass

def clear_all_relationships():
    confirmation = input("Are you sure you want to clear all songs from all playlists? y/n ")
    if confirmation == "y":
        Junction.drop_table()
        print(f"All playlists cleared.")
    else:
         print("Playlists will not be cleared.")

def view_songs_in_playlist():
    playlist_entered = (input("Please enter playlist name: "))
    print(f"Looking for: {playlist_entered}") # debugging
    playlist_retrieved = Playlist.find_by_name(playlist_entered)
    print(f"Found: {playlist_retrieved}") # debugging
    
    if playlist_retrieved:
        songs_in_playlist = Junction.view_songs_in_playlist(playlist_retrieved.id)
        print(f"Songs in playlist {playlist_retrieved.name}: ")
        for song in songs_in_playlist:
            print(f"Title: {song[1]}, Artist: {song[2]}")
    else:
        print("Sorry, playlist not found.")

def exit_program():
    print("Goodbye!")
    exit()