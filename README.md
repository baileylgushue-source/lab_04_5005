# Lab 04 - TV Show Summary

## About the Project

For this lab, I continued working on my TV show project from Lab 03.

My program gets TV show information from TVMaze and creates a summary showing how many shows belong to each genre and language.

For Lab 04, I focused on making my program more reliable and easier to test. I added more tests, error handling, logging, and settings that can be changed without editing the Python code.

I also used tools to check my code for mistakes and formatting issues.

## Data Source

I used TVMaze to get my TV show information.

https://api.tvmaze.com/shows?page=0

My program gets TV show data and selects 10 shows to include in the summary. This number can be changed in the settings file.

## Setup

First, create and activate the Conda environment.

```bash
conda env create -f environment.yml
conda activate lab04-quality
```

Then install the project.

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## How to Run

Run the program using:

```bash
python -m tvsummary.main
```

The program creates a file called `summary.json` inside the `data/processed` folder.

To use a different settings file:

```bash
python -m tvsummary.main --config config/tvsummary.toml
```

## Settings

I created a TOML file to keep my settings in one place.

The file is located at `config/tvsummary.toml`.

It includes:

- URL - Where the TV show information comes from.
- Timeout - How long the program waits for a response.
- Output folder - Where the summary is saved.
- Seed - Helps make the random selection repeatable.
- Sample size - How many shows are selected.
- Log level - Controls which messages are shown.

I used a frozen dataclass to store the settings so they cannot be accidentally changed while the program is running.

## Testing

I used pytest to test different parts of my program.

My tests check things like missing information, genre and language counts, settings errors, and logging messages.

I also tested that using the same random seed gives the same selection.

To run the tests:

```bash
python -m pytest
```

My latest testing session passed 15 tests. I also added tests using a fixture and a temporary folder.

## Check It

I used three tools to check my code.

**pytest** runs my tests to make sure the program works.

```bash
python -m pytest
```

**mypy** checks the types used in my Python code.

```bash
python -m mypy .
```

**Ruff** checks for code problems and formatting.

```bash
python -m ruff check .
python -m ruff format --check .
```

I also used Ruff to automatically format my files.

```bash
python -m ruff format .
```

## Errors and Exit Codes

I added custom errors to make problems easier to understand.

For example, if the settings file is missing, the program shows an error message instead of a long traceback.

The program uses these exit codes:

- **0** - The program finished successfully.
- **1** - An expected error happened, such as a missing settings file.
- **3** - An unexpected error happened.

I also added logging so the program can show information and error messages instead of using print statements.

## Project Files

- `models.py` - Stores information about each TV show.
- `sources.py` - Gets TV show information from TVMaze.
- `aggregations.py` - Counts shows by genre and language.
- `report.py` - Creates and saves the summary.
- `config.py` - Loads the program settings.
- `errors.py` - Contains the custom errors.
- `logging_setup.py` - Sets up logging messages.
- `main.py` - Runs the program.
- `__init__.py` - Makes it easier to import classes.
- `tests/` - Contains the tests.
- `conftest.py` - Contains sample data for testing.
- `pyproject.toml` - Contains project and code-checking settings.
- `environment.yml` - Contains the Conda environment settings.
- `requirements.txt` - Lists the Python packages and their versions.

## Design Choices

I kept my project separated into different files because it makes the code easier to understand and update.

I used inheritance in my aggregation classes. The `Aggregation` class provides a common structure, and the genre and language classes build on it.

I also used polymorphism because the different aggregation classes have their own `compute()` methods. This means I can use the same method name for different types of counting.

If I wanted to add another type of summary later, I could create another aggregation class without changing the whole program.

I used custom errors to make problems easier to identify, and logging to help explain what the program is doing.

## Repeatable Results

I added a random seed so the program can select the same TV shows when the same data and settings are used.

I also added a `run_info` section to the JSON summary.

This records the settings, seed, Python version, and versions of the testing tools.

This makes it easier to understand how the results were created.

## What I Learned

For this lab, I learned how to use pytest to test more parts of my code.

I also learned how to create my own error messages and use logging instead of print statements.

Using mypy and Ruff helped me find mistakes and keep my code organized.

I also learned how to use a TOML file to change settings without changing the Python code.

Overall, this lab helped me understand how to make my project more organized, easier to test, and more reliable.
