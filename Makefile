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

.PNONY: serve
serve: # Run application server in development
	poetry run python3 main.py
