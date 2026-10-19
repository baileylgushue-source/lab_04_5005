# Lab 03 - TV Show Summary

## About the project

For this lab, I took my code from Lab 02 and separated it into different Python files. The program still does the same thing, which is getting TV show information from TVMaze and counting how many shows are in each genre and language.

The main difference is that I used classes and inheritance to organize my code.

## Data Source

I used TVMaze to get my TV show information.

https://api.tvmaze.com/shows?page=0

My program gets 240 TV shows and uses that information to make a summary.

## Setup

```bash
conda env create -f environment.yml
conda activate tvsummary
pip install -r requirements.txt
pip install -e .
```

## How to Run

```bash
python main.py
```

The program creates a file called `summary.json` inside the `data/processed` folder.

## How to Test

```bash
python -m unittest discover -s tests
```

I made two tests to check that my `Show` class works properly, including when information is missing.

## Project Files

- `models.py` - Holds the information for each TV show.
- `sources.py` - Gets the TV show information from TVMaze.
- `aggregations.py` - Counts the shows by genre and language.
- `report.py` - Puts the results together and saves them.
- `config.py` - Keeps the URL, timeout, and output location together.
- `__init__.py` - Lets me import my classes.
- `main.py` - Runs the program.

## What Moved Where

| Lab 02 | Lab 03 |
|---|---|
| `fetch_shows()` | `TVShowSource.fetch_shows()` in `sources.py` |
| `shows_per_genre()` | `GenreAggregation.compute()` in `aggregations.py` |
| `shows_per_language()` | `LanguageAggregation.compute()` in `aggregations.py` |
| `build_summary()` | `build_summary()`

## Test Results

I ran my program and it successfully created the summary.json file.

I also ran my two tests and both passed.

The program counted 240 TV shows, which matches my Lab 02 results.
