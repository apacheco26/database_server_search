from Data import Data


class Show:
    pass

class ShowGenre:
    ALL_GENRES = '--All Genres--'

    def __init__(self, genre):
        self._genre = genre

    def get_genre(self):
        return  self._genre

    @staticmethod
    def fetch_genres():
        return Data.fetch_genres()

class ShowType:
    ALL_TYPES = '--All Types--'

    def __init__(self, types):
        self._type = type

    def get_type(self):
        return self._type

    @staticmethod
    def fetch_types():
        return Data.fetch_types()