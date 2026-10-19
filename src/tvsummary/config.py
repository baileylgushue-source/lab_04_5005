from pathlib import Path
from dataclasses import dataclass
import tomllib
from tvsummary.errors import SettingsError



@dataclass(frozen=True)
class Settings:
    url: str
    timeout: int
    output: Path
    seed: int
    sample_size: int
    log_level: str

URL = "https://api.tvmaze.com/shows?page=0"

TIMEOUT = 10

OUTPUT = Path("data/processed/summary.json")

def load_settings(path="config/tvsummary.toml"):
    try:
        with open(path, "rb") as file:
            data = tomllib.load(file)

        return Settings(
            url=data["url"],
            timeout=data["timeout"],
            output=Path(data["output_dir"]) / "summary.json",
            seed=data["seed"],
            sample_size=data["sample_size"],
            log_level=data["log_level"],
        )

    except FileNotFoundError as error:
        raise SettingsError("Settings file not found") from error

    except KeyError as error:
        raise SettingsError("Missing required setting") from error