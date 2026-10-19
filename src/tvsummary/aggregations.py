class Aggregation:
    """Base class for TV show aggregations."""

    name = ""

    def compute(self, shows):
        return {}


class GenreAggregation(Aggregation):
    """Counts TV shows by genre."""

    name = "shows_per_genre"

    def compute(self, shows):
        genre_amount = {}

        for show in shows:
            for genre in show.genres:
                genre_amount[genre] = genre_amount.get(genre, 0) + 1

        return genre_amount


class LanguageAggregation(Aggregation):
    """Counts TV shows by language."""

    name = "shows_per_language"

    def compute(self, shows):
        language_amount = {}

        for show in shows:
            language = show.language

            if language is not None:
                language_amount[language] = language_amount.get(language, 0) + 1

        return language_amount