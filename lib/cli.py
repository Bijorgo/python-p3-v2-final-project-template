#!/usr/bin/env python3

from helpers import (
    exit_program,
    helper_1
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
            pass
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
