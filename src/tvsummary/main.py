import argparse
import logging

from tvsummary import TVShowSource
from tvsummary.config import load_settings
from tvsummary.errors import TVSummaryError
from tvsummary.logging_setup import setup_logging
from tvsummary.report import build_summary, write_summary

logger = logging.getLogger(__name__)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        default="config/tvsummary.toml",
    )
    args = parser.parse_args(argv)

    setup_logging()

    try:
        settings = load_settings(args.config)
        logging.getLogger().setLevel(settings.log_level)

        logger.info("Starting TV show summary")

        source = TVShowSource(settings.url)
        shows = source.fetch_shows()

        summary = build_summary(shows, settings.url)

        settings.output.parent.mkdir(parents=True, exist_ok=True)
        write_summary(summary, settings.output)

        logger.info("Summary written to %s", settings.output)
        return 0

    except TVSummaryError as error:
        logger.error("Application error: %s", error)
        return 1

    except Exception:  # noqa: BLE001 - Main handles unexpected errors with exit code 3.
        logger.error("Unexpected application error", exc_info=False)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
