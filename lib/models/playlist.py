class Playlist:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) and len(name) > 0:
            raise ValueError("Name must be a string of 1 or more characters")
        self._name = name

    @description.setter
    def description(self, description):
        if not isinstance(description, str) and ( 0 <= len(description) <= 50):
            raise ValueError("Description must be a string between 0 and 50 characters")