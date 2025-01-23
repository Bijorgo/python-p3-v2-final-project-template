# lib/playlist_helpers.py

from playlist_helpers import (
    create_new_playlist,
    delete_playlist,
    display_all_playlists,
    find_playlist_by_name,
    update_playlist_info,
    delete_all_playlists
)

from song_helpers import (
    create_new_song,
    delete_song,
    display_all_songs,
    find_song_by_title,
    update_song_info,
    delete_all_songs
)

from junction_helpers import (
    adding_song_to_playlist,
    clear_all_relationships,
    view_songs_in_playlist,
    remove_song_from_playlist,
    master_reset
)

def create_new():
    print("What would you like to create?")
    print("1. Playlist")
    print("2. Song")
    choice = input("Create a: ").strip()
    if choice == '1':
        create_new_playlist()
    elif choice == '2':
        create_new_song()
    else:
        print("Invalid choice")

def update_info():
    print("What would you like to update?")
    print("1. Playlist")
    print("2. Song")
    choice = input("Update a: ").strip()
    if choice == '1':
        update_playlist_info()
    elif choice == '2':
        update_song_info()
    else:
        print("Invalid choice")

def look_up():
    print("What would you like to look up?")
    print("1. Playlist")
    print("2. Song")
    choice = input("Find a: ").strip()
    if choice == '1':
        find_playlist_by_name()
    elif choice == '2':
        find_song_by_title()
    else:
        print("Invalid choice")

def display_all():
    print("What would you like to display?")
    print("1. Playlists")
    print("2. Songs")
    choice = input("Display all: ")
    if choice == '1':
        display_all_playlists()
    elif choice == '2':
        display_all_songs()
    else:
        print("Invalid choice")

def delete():
    print("What would you like to delete?")
    print("1. Playlist")
    print("2. Song")
    print("3. All Playlists")
    print("4. All Songs")
    print("5. Clear All Songs From All Playlists")
    print("6. MASTER RESET")
    choice = input("Delete: ").strip()
    if choice == '1':
        delete_playlist()
    elif choice == '2':
        delete_song()
    elif choice == '3':
        delete_all_playlists()
    elif choice == '4':
        delete_all_songs()
    elif choice == '5':
        clear_all_relationships()
    elif choice == '6':
        master_reset()
    else:
        print("Invalid choice")

def playlist_contents():
    print("What would you like to do?")
    print("1. Add Song To Playlist")
    print("2. Remove Song From Playlist")
    print("3. View Songs In Playlist")
    choice = input("Choice: ").strip()
    if choice == '1':
        adding_song_to_playlist()
    elif choice == '2':
        remove_song_from_playlist()
    elif choice == '3':
        view_songs_in_playlist()
    else:
        print("Invalid choice")

def exit_program():
    print("Goodbye!")
    exit()