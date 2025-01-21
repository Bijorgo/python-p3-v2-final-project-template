# lib/song_helpers.py

from models.song import Song

def create_new_song():
    Song.create_table() # Check if table exist, if no: create table
    title = input("Ener song title: ").strip().lower() # All inputs will be stored lowercased, no trailing whitespaces
    artist = input("Enter artist name: ").strip().lower()
    genre = input("Enter genre: ").strip().lower()
    duration = input("Enter duration: ").strip().lower()
    try:
        Song.create(title, artist, genre, duration)
    except Exception as exc:
        print("Error creating song: ", exc)

def find_song():
    Song.create_table() # Check if table exists, if no: create one
    given_title = input("Enter song title: ").strip().lower()
    given_artist = input("Enter artist name: ").strip().lower()
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
        print(f"Song found!")
        print(f"Title: {song.title}, Artist: {song.artist}, Genre: {song.genre}, Duration: {song.duration}")
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
            new_title = input("Enter the new title: ").strip().lower()
            if not isinstance(new_title, str) or not 0 <= len(new_title):
                raise TypeError("Song title must be a string of 1 or more characters.")
            song.title = new_title
        elif choice == '2':
            new_artist = input("Enter the new artist: ").strip().lower()
            if not isinstance(new_artist, str) or not 0 <= len(new_artist):
                raise TypeError("Song artist must be a string of 1 or more characters.")
            song.artist = new_artist
        elif choice == '3':
            new_genre = input("Enter the new genre: ").strip().lower()
            if not isinstance(new_genre, str) or not 0 <= len(new_genre):
                raise TypeError("Song genre must be a string of 1 or more characters.")
            song.genre = new_genre
        elif choice == '4':
            new_duration = input("Enter the new duration: ").strip().lower()
            if not isinstance(new_duration, (int, float)):
                raise TypeError("Song duration must be a decimal number.")
            song.duration = new_duration
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
