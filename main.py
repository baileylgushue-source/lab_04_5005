from tvsummary import TVShowSource
from tvsummary.config import URL, OUTPUT
from tvsummary.report import build_summary, write_summary


def main():
    try:
        source = TVShowSource(URL)
        shows = source.fetch_shows()

        summary = build_summary(shows, URL)

        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        write_summary(summary, OUTPUT)

        print("Summary written to", OUTPUT)

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()