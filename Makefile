run:
	poetry run uvicorn app.main:app --reload

setup:
	source venv/bin/activate
	poetry install