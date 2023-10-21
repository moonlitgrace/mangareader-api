dev: # run uvicorn server
	poetry run python3 main.py

poetry: # install deps from poetry
	poetry install
