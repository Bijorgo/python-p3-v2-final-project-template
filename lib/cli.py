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
    update_song_info,
    delete_all_songs
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
        if choice == "EXIT":
            exit_program()
        elif choice == "1":
            create_new_playlist()
        elif choice == "2":
            update_playlist_info
        elif choice == "3":
            display_all_playlists() 
        elif choice == "4":
            find_playlist_by_name()
        elif choice == "5":
            adding_song_to_playlist()
        elif choice == "6":
            view_songs_in_playlist()   
        elif choice == "7":
            create_new_song()
        elif choice == "8":
            update_song_info()     
        elif choice == "9":
            display_all_songs()
        elif choice == "10":
            find_song_by_title()               
        elif choice == "11":
            delete_playlist()
        elif choice == "12":
            delete_song()
        elif choice == "13":
            delete_all_songs()
        elif choice == "14":
            pass
        elif choice == "15":
            clear_all_relationships()
        else:
            print("Invalid choice")
        
        
        
        
        
        


def menu():
    print("Please select an option:")
    print("~~~~PLAYLIST OPTIONS:~~~~")
    #print("~~~~~~~~~~~~~~~~~~~~~")
    print("1. Create New Playlist")
    print("2. Update playlist")
    print("3. Display all Playlists")
    print("4. Find A Playlist")
    print("5. Add Song to Playlist")
    print("6. View Songs In Playlist")
    print("~~~~SONG OPTIONS:~~~~")
    #print("~~~~~~~~~~~~~~~~~~~~~")
    print("7. Create A Song")
    print("8. Update song")
    print("9. Display All Songs")
    print("10. Find A Song")
    print("~~~~DELETE OPTIONS~~~~")
    #print("~~~~~~~~~~~~~~~~~~~~~")
    print("11. Delete Playlist")
    print("12. Delete A Song")
    print("13. Delete All Songs")
    print("14. Delete All Playlists")
    print("15. Clear All Songs In All Playlists")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("EXIT to Exit the program")


if __name__ == "__main__":
    main()
