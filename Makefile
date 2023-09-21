run: # run uvicorn server
	poetry run uvicorn app.main:app --reload

install: # install deps from poetry
	poetry install
