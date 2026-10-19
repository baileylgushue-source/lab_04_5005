import unittest

import pytest

from tvsummary.aggregations import GenreAggregation, LanguageAggregation
from tvsummary.models import Show


class TestShow(unittest.TestCase):
    def test_genres(self):
        show = Show(["Drama"], "English")
        self.assertEqual(show.genres, ["Drama"])

    def test_missing_values(self):
        show = Show(None, None)
        self.assertEqual(show.genres, [])
        self.assertIsNone(show.language)

    def test_invalid_genres(self):
        show = Show("Drama", "English")
        self.assertEqual(show.genres, [])

    def test_missing_genres(self):
        show = Show(None, "English")
        self.assertEqual(show.genres, [])

    def test_missing_rating(self):
        show = Show(["Drama"], "English")
        self.assertIsNone(show.rating)

    def test_genre_aggregation(self):
        shows = [Show(["Drama"], "English"), Show(["Drama", "Comedy"], "English")]

        result = GenreAggregation().compute(shows)

        self.assertEqual(result, {"Drama": 2, "Comedy": 1})

    def test_language_aggregation(self):
        shows = [
            Show(["Drama"], "English"),
            Show(["Comedy"], "Spanish"),
            Show(["Drama"], "English"),
        ]

        result = LanguageAggregation().compute(shows)

        self.assertEqual(result, {"English": 2, "Spanish": 1})


if __name__ == "__main__":
    unittest.main()


@pytest.mark.parametrize(
    "language, expected",
    [
        ("English", "English"),
        ("French", "French"),
        (None, None),
        (12345, None),
    ],
)
def test_show_language(language, expected):
    show = Show(["Drama"], language)
    assert show.language == expected


def test_load_settings():
    from tvsummary.config import load_settings

    settings = load_settings()

    assert settings.timeout == 10
    assert settings.seed == 42
    assert settings.sample_size == 10


def test_missing_settings_file():
    import pytest

    from tvsummary.config import load_settings
    from tvsummary.errors import SettingsError

    with pytest.raises(SettingsError, match="Settings file not found"):
        load_settings("missing.toml")


def test_settings_error_logging(caplog):
    import logging

    import pytest

    from tvsummary.config import load_settings
    from tvsummary.errors import SettingsError

    with caplog.at_level(logging.ERROR), pytest.raises(SettingsError):
        load_settings("missing.toml")

    assert "Settings file not found" in caplog.text


def test_seeded_sampling():
    import random

    shows = ["A", "B", "C", "D", "E"]

    first = random.Random(42).sample(shows, 3)
    second = random.Random(42).sample(shows, 3)

    assert first == second


def test_sample_shows_fixture(sample_shows):
    assert len(sample_shows) == 3
    assert "Show A" in sample_shows


def test_tmp_path(tmp_path):
    file = tmp_path / "test_summary.txt"
    file.write_text("TV show summary")

    assert file.read_text() == "TV show summary"
