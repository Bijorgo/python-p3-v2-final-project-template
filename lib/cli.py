#!/usr/bin/env python3

from playlist_helpers import (
    exit_program,
    create_new_playlist,
    delete_playlist,
    display_all_playlists,
    find_playlist_by_name
)

from song_helpers import (
    create_new_song,
    delete_song,
    display_all_songs,
    find_song_by_title
)

from junction_helpers import (
    adding_song_to_playlist
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_new_playlist()
        elif choice == "2":
            delete_playlist()
        elif choice == "3":
            display_all_playlists()
        elif choice == "4":
            find_playlist_by_name()
        elif choice == "5":
            create_new_song()
        elif choice == "6":
            delete_song()
        elif choice == "7":
            display_all_songs()
        elif choice == "8":
            find_song_by_title()
        elif choice == "9":
            adding_song_to_playlist()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create New Playlist")
    print("2. Delete Playlist")
    print("3. Display all Playlists")
    print("4. Find A Playlist")
    print("5. Add A Song")
    print("6. Delete A Song")
    print("7. Display All Songs")
    print("8. Find A Song")
    print("9. Add Song to Playlist")


if __name__ == "__main__":
    main()
