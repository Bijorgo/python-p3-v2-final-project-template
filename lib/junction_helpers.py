# lib/junction_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def find_relation():
    Junction.create_table() # Check if table exist, if no: create table
    Playlist.create_table()
    Song.create_table()
    # Input playlist
    playlist_entered = input("Enter playlist name: ")
    playlist_found = Playlist.find_by_name(playlist_entered)
    #print(f"Query result: {playlist_found}") #debugging
    # Input song
    song_title_entered = input("Enter song title: ")
    song_artist_entered = input("Enter song artist: ")
    song_found = Song.find_one_song(song_title_entered, song_artist_entered)
    # Return matching relation if one exists
    return song_found, playlist_found, playlist_entered, song_title_entered

def adding_song_to_playlist():
    song_found, playlist_found, song_entered, playlist_entered,  = find_relation()    
    # Try adding song playlist relationship
    if playlist_found and song_found:
            try:
                Junction.add_song_to_playlist(playlist_found.id, song_found.id)
            except Exception as exc:
                print(f"Error adding {song_found} to {playlist_found}.", exc)
    else:
        print(f"Sorry, playlist `{playlist_entered}` or `{song_entered} not found.")

def remove_song_from_playlist():
    song_found, playlist_found, song_entered, playlist_entered,  = find_relation()    
    # Try removing song playlist relationship
    if playlist_found and song_found:
        try:
            Junction.remove_song_from_playlist(playlist_found.id, song_found.id)
            print("Done") # debugging
        except Exception as exc:
            print(f"Error removing {song_entered} from {playlist_entered}.", exc)

def clear_all_relationships():
    confirmation = input("Are you sure you want to clear all songs from all playlists? y/n ")
    if confirmation == "y":
        Junction.drop_table()
    else:
         print("Playlists will not be cleared.")

def view_songs_in_playlist():
    playlist_entered = input("Please enter playlist name: ").strip().lower()
    #print(f"Looking for: {playlist_entered}") # debugging
    playlist_retrieved = Playlist.find_by_name(playlist_entered)
    #print(f"Found: {playlist_retrieved}") # debugging
    
    if playlist_retrieved:
        songs_in_playlist = Junction.view_songs_in_playlist(playlist_retrieved.id)
        if songs_in_playlist:
            print(f"Songs in playlist {playlist_retrieved.name}: ")
            for song in songs_in_playlist:
                print(f"Title: {song[1]}, Artist: {song[2]}")
    else:
        print("Sorry, playlist not found.")

def master_reset():
    # This function drops all tables
    confirmation = input("Are you sure you want to delete all data tables? Please type: `MASTER RESET` : ")
    if confirmation == "MASTER RESET":
        # Drop tables
        Playlist.drop_table
        Song.drop_table()
        Junction.drop_table()
        # Reset all dictionaries
        Song.all_songs.clear()
        Playlist.all_playlists.clear()
        print("All tables dropped.")
    else:
        print("No changes made.")