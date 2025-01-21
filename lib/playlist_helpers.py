# lib/playlist_helpers.py
from models.playlist import Playlist
from models.song import Song
from models.junction import Junction

def find_playlist():
    Playlist.create_table() # Check if table exist, if no: create table
    given_name = input("Enter playlist name: ").strip().lower()   
    playlist = Playlist.find_by_name(given_name) 
    return playlist, given_name

def create_new_playlist():
    Playlist.create_table()  # Check if table exist, if no: create table
    name = input("Enter playlist name: ").strip().lower() 
    description = input("Enter playlist description: ").strip().lower()
    try:
        Playlist.create(name, description) # Create new playlist instance
    except Exception as exc:
        print("Error creating playlist: ", exc)

def delete_playlist():
    Playlist.create_table()
    playlist, given_name = find_playlist()
    if playlist:
        playlist.delete()
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
    playlist, given_name = find_playlist()
    if playlist:
        print(playlist)
    else:
        print(f"Sorry, playlist {given_name} not found.")

def delete_all_playlists():
    confirm = input("Are you sure you want to delete all playlists? y/n ").strip().lower()
    if confirm == "y":
        Playlist.drop_table()
    else:
        print("Playlists were not deleted.")

def update_playlist_info():
    # Find playlist based on input
    playlist, given_name = find_playlist()
    # If playlist is found, choose how to update
    if playlist:
        # Ask user which detail to update
        print("What would you like to update?")
        print("1. Name")
        print("2. Description")
        choice = input("Enter the number of the field you want to update: ").strip()
        
        # Update the chosen field
        if choice == '1':
            new_name = input("Enter the new name: ").strip().lower()
            playlist.name = new_name
        elif choice == '2':
            new_description = input("Enter the new description: ").strip().lower()
            playlist.description = new_description
        else:
            print("Invalid choice. No changes made.")
            return
        
        # Save the updated playlist record
        try:
            playlist.save()
            print(f"Playlist updated successfully: Name: {playlist.name}, Description: {playlist.description}")
        except Exception as exc:
            print("Error updating playlist: ", exc)
    else:
        print(f"Song {given_name} not found.")      