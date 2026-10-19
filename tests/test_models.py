import unittest
from tvsummary.models import Show


class TestShow(unittest.TestCase):

    def test_genres(self):
        show = Show(["Drama"], "English")
        self.assertEqual(show.genres, ["Drama"])

    def test_missing_values(self):
        show = Show(None, None)
        self.assertEqual(show.genres, [])
        self.assertIsNone(show.language)


if __name__ == "__main__":
    unittest.main()