# Playlist Manager

## Description

The Playlist Manager is a Python-based command-line interface (CLI) application that allows users to manage playlists and songs. It provides functionality to:

- Create, update, and delete playlists and songs.
- Add and remove songs from playlists with a many-to-many relationship.
- View all playlists or songs.
- Find playlists by name or songs by title/artist.
- Perform a "master reset" to clear all tables and relationships.

## Technologies Used

- **Python**: The primary programming language for the application.
- **SQLite**: The database used to store playlists, songs, and their relationships.
- **Pipenv**: Used to manage dependencies in a virtual environment.

## Installation

To install and set up the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2. Install the dependencies using `pipenv`:

    ```bash
    pipenv install
    pipenv shell
    ```

3. Run the CLI by executing:

    ```bash
    python lib/cli.py
    ```

## Usage

Once the application is running, you will be presented with a menu. You can interact with the CLI to manage playlists and songs as follows:

### Main Menu

```text
~~~~~~~~~~~~~~~~~~~~~
~~Please select an option: ~~
~~~~~~~~~~~~~~~~~~~~~
1. Create Playlist or Song
2. Update Playlist Or Song
3. Look Up Playlist Or Song
4. Display All Playlists or Songs
5. Playlist Contents
6. Delete Options
~~~~~~~~~~~~~~~~~~~~~
EXIT to Exit the program
```

### Available Options:
Create Playlist or Song:

Create a new playlist or song by providing necessary details (e.g., title, artist, genre).
Update Playlist Or Song:

Update the name, description, or other details of an existing playlist or song.
Look Up Playlist Or Song:

Find a playlist by its name or search for a song by its title.
Display All Playlists or Songs:

View all the available playlists or songs stored in the database.
Playlist Contents:

Add or remove songs from playlists or view the songs in a specific playlist.
Delete Options:

Delete a specific playlist or song, or clear all playlists, songs, or relationships between them. You can also perform a "MASTER RESET" to clear all data.
Example Commands:
Create Playlist:

Select option 1 and choose "Playlist" to create a new playlist.
Add Song to Playlist:

Select option 5 ("Playlist Contents"), then choose option 1 to add a song to a playlist.
Delete Playlist:

Select option 6, then option 1 to delete a specific playlist.
Master Reset:

Select option 6, then option 6 to perform a master reset, clearing all tables and relationships.

## Directory Structure
The project follows the structure below:

```
playlist-manager/
│
├── lib/
│   ├── models/
│   │   ├── __init__.py       # Initialization for the models
│   │   ├── junction.py       # Junction table model for playlist-song relationships
│   │   ├── playlist.py       # Playlist model
│   │   └── song.py           # Song model
│   ├── cli.py                # Entry point for the application (CLI)
│   ├── database.py           # Database connection and setup
│   ├── debug.py              # Debugging utilities
│   ├── general_helpers.py    # General helper functions
│   ├── junction_helper.py    # Helper functions for playlist-song relationships
│   ├── playlist_helpers.py   # Helper functions for playlist management
│   ├── song_helpers.py       # Helper functions for song management
│
└── README.md                 # Project documentation
```



## No License
This project is for educational purposes and does not have a formal license.

### Note: This is a school project and is not accepting contributions at this time.

