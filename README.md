# `manga-api`

Python-based web scraping tool built with FastAPI that provides easy access to manga content from different providers.  
This API allows users to retrieve up-to-date information about various manga titles, chapters, and pages(under-development), enabling developers to create their own manga-related applications and services.

## API Guide

Detailed documentation: [**API ReDoc**](https://manga-apiv1.vercel.app/redoc)\
Interactive documentation: [**API Doc**](https://manga-apiv1.vercel.app/docs) (try API)

## Local Setup

### Poetry
We use [poetry](https://python-poetry.org/) as our package manager. So make sure you've poetry installed.\
Also we use [gnu make](https://www.gnu.org/software/make/) (optional)

**Step 1**: Clone this repo and `cd` into root directory.\
**Step 2**: Setup `poetry`
```bash
poetry install
# or make poetry
```
**Step 3**: Finally run app
```bash
poetry run python3 main.py
# or make dev
```

### Pip
**Step 1**: Clone this repo and `cd` into root directory.\
**Step 2**: Create a virtual env (recommended) and activate it ([venv](https://docs.python.org/3/library/venv.html))\
**Step 3**: Install dependencies
```bash
pip install -r requirements.txt
```
**Step 4**: Finally run app with `python3 main.py`

## Contribution

Contributions to manga api are welcome!\
If you encounter issues or want to add new features, feel free to open pull requests.\
Give a ⭐️ if you find this project interesting and useful!

## Disclaimer

This project is developed for educational purposes and convenience in accessing manga content.\
Respect the website's terms of use and consider the legality of web scraping in your jurisdiction.
