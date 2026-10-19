import json

from .aggregations import GenreAggregation, LanguageAggregation


def build_summary(shows, url):
    """Create a summary of the TV shows."""

    summary = {
        "source_url": url,
        "records_processed": len(shows)
    }

    for aggregation in [GenreAggregation(), LanguageAggregation()]:
        summary[aggregation.name] = aggregation.compute(shows)

    return summary


def write_summary(summary, path):
    """Save the summary as a JSON file."""
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")