class Playlist:
    all_playlists = []
    def __init__(self, name, description):
        self.id = None  # id will be set in database
        self._name = name
        self._description = description

    # All proprty attributes
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    # All property setters
    @name.setter
    def name(self, name):
        if not isinstance(name, str) and len(name) > 0:
            raise ValueError("Name must be a string of 1 or more characters")
        self._name = name

    @description.setter
    def description(self, description):
        if not isinstance(description, str) and ( 0 <= len(description) <= 50):
            raise ValueError("Description must be a string between 0 and 50 characters")
    
    # Methods
    @classmethod
    def create(self, name, description):
        Playlist(name, description)
        Playlist.all_playlists.append(self)

    @classmethod
    def delete(self):
        pass

    @classmethod
    def get_all():
        pass

    @classmethod
    def view_songs():
        pass

    @classmethod
    def add_song():
        pass

    @classmethod
    def remove_song():
        pass

    @classmethod
    def find_by_attribute():
        pass