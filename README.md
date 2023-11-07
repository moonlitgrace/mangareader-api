# manga-api

Python-based web scraping tool built with FastAPI that provides easy access to manga content from the mangareader.to website. This API allows users to retrieve up-to-date information about various manga titles, chapters, and pages, enabling developers to create their own manga-related applications and services.

### API Guide

Detailed documentation: [**API ReDoc**](https://manga-apiv1.vercel.app/redoc)\
Interactive documentation: [**API Doc**](https://manga-apiv1.vercel.app/docs) (try API)

### Local Setup

#### Poetry (recommended)
We use [poetry](https://python-poetry.org/) as our package manager. So make sure you've poetry installed.\
Also we use [gnu make](https://www.gnu.org/software/make/) (optional)

**Step 1**: Clone this repo and `cd` into root directory.\
**Step 2**: Setup `poetry`
```bash
poetry install
# or make poetry
```
**Step 3**: Activate `poetry shell`\
**Step 4**: Finally run app
```bash
poetry run python3 main.py
# or make dev
```

#### Pip
**Step 1**: Clone this repo and `cd` into root directory.\
**Step 2**: Create a virtual env (recommended) and activate it ([venv](https://docs.python.org/3/library/venv.html))\
**Step 3**: Install dependencies
```bash
pip install -r requirements.txt
```
**Step 4**: Finally run app with `python3 main.py`

**Done, now you're good to go!**

### Contribution

Contributions to MangaAPI are welcome!\
If you encounter issues or want to add new features, feel free to open pull requests.\
Give a ⭐️ if you find this project interesting and useful!

### Disclaimer

This project is developed for educational purposes and convenience in accessing manga content.\
Respect the website's terms of use and consider the legality of web scraping in your jurisdiction.

### License
```
MIT License

Copyright (c) 2023 Tokito

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
