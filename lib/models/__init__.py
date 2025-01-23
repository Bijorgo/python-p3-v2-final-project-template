# lib/models/__init__.py

import sqlite3

CONN = sqlite3.connect('playlist_manager.db')
CURSOR = CONN.cursor()
