# This Makefile is totally based on poetry
# So please make sure you've poetry installed

.PNONY: install
install: # Install dependencies
	poetry install

.PNONY: update
update: # Update dependencies
	poetry update

.PNONY: show
show: # Show environment details
	poetry env info

.PNONY: shell
shell: # Enter into venv shell
	poetry shell

.PNONY: dev
dev: # Run application server in development
	poetry run fastapi dev main.py

.PNONY: format
black: # Run black
	poetry run black

.PNONY: requirements
requirements: # Generate requirements.txt file
	poetry run pip freeze > requirements.txt
