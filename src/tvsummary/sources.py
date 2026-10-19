import requests
from .models import Show


class TVShowSource:
    """Downloads TV shows from TVMaze."""

    def __init__(self, url):
        self.url = url

    def fetch_shows(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()

        records = response.json()
        shows = []

        for record in records:
            show = Show(
                record.get("genres"),
                record.get("language")
            )
            shows.append(show)

        return shows