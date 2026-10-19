import unittest
from tvsummary.models import Show
from tvsummary.aggregations import GenreAggregation
from tvsummary.aggregations import LanguageAggregation

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
        shows = [
            Show(["Drama"], "English"),
            Show(["Drama", "Comedy"], "English")
        ]

        result = GenreAggregation().compute(shows)

        self.assertEqual(result, {"Drama": 2, "Comedy": 1})

    def test_language_aggregation(self):
        shows = [
            Show(["Drama"], "English"),
            Show(["Comedy"], "Spanish"),
            Show(["Drama"], "English")
        ]

        result = LanguageAggregation().compute(shows)

        self.assertEqual(result, {"English": 2, "Spanish": 1})


if __name__ == "__main__":
    unittest.main()