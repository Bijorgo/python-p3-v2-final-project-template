# lib/playlist_helpers.py
from models.playlist import Playlist

def create_new_playlist():
    Playlist.create_table()  
    name = input("Enter playlist name: ").strip().lower() # All inputs will be stored lowercased, no trailing white space
    description = input("Enter playlist description: ").strip().lower()
    try:
        Playlist.create(name, description) # Create new playlist instance
    except Exception as exc:
        print("Error creating playlist: ", exc)

def find_playlist():
    Playlist.create_table() # Check if table exist, if no: create table
    given_name = input("Enter playlist name: ").strip().lower()   
    playlist = Playlist.find_by_name(given_name) # Find playlist based on input
    return playlist, given_name

def delete_playlist():
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
    # Confirm delete selection
    confirm = input("Are you sure you want to delete all playlists? y/n ").strip().lower()
    if confirm == "y":
        Playlist.drop_table()
    else:
        print("Playlists were not deleted.")

def update_playlist_info():
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
            # Data type validation
            if not isinstance(new_name, str) or not 0 <= len(new_name):
                raise TypeError("Playlist name must be a string of 1 or more characters.") 
            playlist.name = new_name
        elif choice == '2':
            new_description = input("Enter the new description: ").strip().lower()
            if not isinstance(new_description, str) or not ( 0 < len(new_description) <= 50):
                raise TypeError("Playlist description must be a string between 0 and 50 characters") 
            playlist.description = new_description
        else:
            print("Invalid choice. No changes made.")
            return
        # Save the updated playlist record
        try:
            playlist.update()
        except Exception as exc:
            print("Error updating playlist: ", exc)
    else:
        print(f"Song {given_name} not found.")      