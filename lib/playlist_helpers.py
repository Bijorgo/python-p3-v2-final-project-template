# lib/playlist_helpers.py
from models.playlist import Playlist
from validations import validate_non_empty_string, validate_input

def create_new_playlist():
    Playlist.create_table() 
    # Validate name input
    name = validate_input("Enter playlist name: ", validate_non_empty_string, "Name must be one or more chracters")
       
    # Default description input to None if no input 
    description = input("Enter playlist description: ".strip().lower())
    if not description:
        description = None # Default description to None

    # Try to create new playlist instance
    try:
        Playlist.create(name, description) # Create new playlist instance
    except Exception as exc:
        print("Error creating playlist: ", exc)

def find_playlist():
    Playlist.create_table() # Check if table exist, if no: create table
    given_name = validate_input("Enter playlist name: ", validate_non_empty_string, "No input, try again").strip().lower()
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
        print(f"Playlist found: {playlist}")
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
            new_name = validate_input("Enter new playlist name: ", validate_non_empty_string, "Name must be a string of 1 or more characters.")
            try:
                playlist.name = new_name
            except ValueError as verr:
                print(f"Error: {verr}")
                return
        elif choice == '2':
            new_description = input("Enter the new description: ").strip().lower()
            #if not new_description:
                #new_description = None # Default to None
            playlist.description = new_description
        else:
            print("Invalid choice. No changes made.")
            return
        # Save the updated playlist record
        try:
            playlist.update()
        except Exception as exc:
            print("Error updating playlist: ", exc)
    #else:
        #print(f"Playlist {given_name} not found.")      