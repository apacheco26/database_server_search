

class Data:
    _connection = None

    @classmethod
    def fetch_genres(cls):
        from Show import ShowGenre
        return [
            ShowGenre("Sci-FI"),
            ShowGenre("Comedy"),
            ShowGenre("Fantasy"),
            ShowGenre("Biography")
        ]

    @classmethod
    def fetch_types(cls):
        from Show import ShowType

        return [
            ShowType("movie"),
            ShowType("tvSeries"),
            ShowType("tvShort"),
            ShowType("tvEpisode")
        ]

