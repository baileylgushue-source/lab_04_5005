class Show:
    """Represents one TV show."""

    def __init__(self, genres, language):
        if isinstance(genres, list):
            self.genres = genres
        else:
            self.genres = []

        if isinstance(language, str):
            self.language = language
        else:
            self.language = None

    def __str__(self):
        return f"TV Show: {self.language}"