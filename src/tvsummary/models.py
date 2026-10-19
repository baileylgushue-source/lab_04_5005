class Show:
    """Represents one TV show."""

    def __init__(self, genres, language, rating=None):
        if isinstance(genres, list):
            self.genres = genres
        else:
            self.genres = []

        if isinstance(language, str):
            self.language = language
        else:
            self.language = None

        self.rating = rating

    def __str__(self):
        return f"TV Show: {self.language}"


def test_missing_settings_file():
    import pytest

    from tvsummary.config import load_settings
    from tvsummary.errors import SettingsError

    with pytest.raises(SettingsError, match="Settings file not found"):
        load_settings("missing.toml")
