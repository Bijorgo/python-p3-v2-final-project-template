#!/usr/bin/env python3

from playlist_helpers import (
    create_new_playlist,
    delete_playlist,
    display_all_playlists,
    find_playlist_by_name,
    update_playlist_info
)

from song_helpers import (
    create_new_song,
    delete_song,
    display_all_songs,
    find_song_by_title,
    update_song_info
)

from junction_helpers import (
    adding_song_to_playlist,
    clear_all_relationships,
    view_songs_in_playlist,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_new_playlist()
        elif choice == "update playlist":
            update_playlist_info
        elif choice == "2":
            delete_playlist()
        elif choice == "3":
            display_all_playlists()
        elif choice == "4":
            find_playlist_by_name()
        elif choice == "5":
            create_new_song()
        elif choice == "update song":
            update_song_info()
        elif choice == "6":
            delete_song()
        elif choice == "7":
            display_all_songs()
        elif choice == "8":
            find_song_by_title()
        elif choice == "9":
            adding_song_to_playlist()
        elif choice == "10":
            view_songs_in_playlist()
        elif choice == "11":
            clear_all_relationships()
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
    print("10. View Songs In Playlist")
    print("11. Clear All Songs In All Playlists")
    print("update playlist")
    print("update song")


if __name__ == "__main__":
    main()
