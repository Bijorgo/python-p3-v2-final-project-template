#!/usr/bin/env python3

from general_helpers import(
    create_new,
    update_info,
    look_up,
    display_all,
    delete,
    playlist_contents,
    exit_program
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "EXIT":
            exit_program()
        elif choice == "1":
            create_new()
        elif choice == "2":
            update_info()
        elif choice == "3":
            look_up()
        elif choice == "4":
            display_all()
        elif choice == "5":
            playlist_contents()
        elif choice == "6":
            delete()
        else:
            print("Invalid choice")   


def menu():
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("~~Please select an option: ~~")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("1. Create Playlist or Song")
    print("2. Update Playlist Or Song")
    print("3. Look Up Playlist Or Song")
    print("4. Display All Playlists or Songs")
    print("5. Playlist Contents") 
    print("6. Delete Options")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("EXIT to Exit the program")


if __name__ == "__main__":
    main()
