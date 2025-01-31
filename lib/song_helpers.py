# lib/song_helpers.py

from models.song import Song
from validations import validate_non_empty_string, validate_input

def create_new_song():
    Song.create_table() # Check if table exist, if no: create table
    # Validate title input
    title = validate_input("Enter song title: ", validate_non_empty_string,  "Title must be a string of 1 or more characters.")
    # Validate artist input
    artist = validate_input("Enter artist name: ", validate_non_empty_string,  "Name must be a string of 1 or more characters.")
    # Take genre input, default to None
    genre = str(input("Enter genre: ").strip().lower())
    if not genre:
        genre = None # Default genre to None
    # Take duration input, default to None
    duration = input("Enter duration: ").strip().lower()
    if  isinstance(duration, (float, int)):
        duration = float(duration)  # Convert to float
    else:
        duration = None # All other values default to None
    # Try to create new instance
    try:
        Song.create(title, artist, genre, duration)
    except Exception as exc:
        print("Error creating song: ", exc)

def find_song():
    Song.create_table() # Check if table exists, if no: create one
    given_title = validate_input("Enter song title: ", validate_non_empty_string, "No input, try again").strip().lower()
    given_artist = validate_input("Enter artist name: ", validate_non_empty_string, "No input, try again").strip().lower()
    song = Song.find_one_song(given_title, given_artist)
    return song, given_title, given_artist        

def delete_song():
    song, given_title, given_artist = find_song()
    if song:
        song.delete()
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
    song, given_title, given_artist = find_song()
    if song:
        print(f"Song found! \nTitle: {song.title}, Artist: {song.artist}, Genre: {song.genre}, Duration: {song.duration}")
    else:
        print(f"Sorry, {given_title} not found")

def delete_all_songs():
    # Confirm delete selection
    confirm = input("Are you sure you want to delete all songs? y/n ").strip().lower()
    if confirm == "y":
        Song.drop_table()
    else:
        print("Songs were not deleted.")

def update_song_info():
    # Find song based on input
    song, given_title, given_artist = find_song()
    # If song is found, choose how to update
    if song:
        # Ask user which detail to update
        print("What would you like to update?")
        print("1. Title")
        print("2. Artist")
        print("3. Genre")
        print("4. Duration")
        choice = input("Enter the number of the field you want to update: ").strip()
        
        # Update the chosen field
        if choice == '1':
            new_title = validate_input("Enter song title: ", validate_non_empty_string,  "Title must be a string of 1 or more characters.")
            song.title = new_title
        elif choice == '2':
            new_artist = validate_input("Enter artist name: ", validate_non_empty_string,  "Name must be a string of 1 or more characters.")
            song.artist = new_artist
        elif choice == '3':
            new_genre = input("Enter the new genre: ").strip().lower()
            if not new_genre:
                new_genre = None # Default to none
            song.genre = new_genre
        elif choice == '4':
            new_duration = input("Enter the new duration: ").strip()
            if isinstance(new_duration, (int, float)):
                new_duration = float(duration)  # Convert to float if it's an integer
            else:
                    duration = None # All other data types default to None
        else:
            print("Invalid choice. No changes made.")
            return
        # Save the updated song record
        try:
            song.update()
            print(f"Song updated successfully: Title: {song.title}, Artist: {song.artist}, Genre: {song.genre}, Duration: {song.duration}")
        except Exception as exc:
            print("Error updating song: ", exc)
    else:
        print(f"Song {given_title} by {given_artist} not found.")
