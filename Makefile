helloworld:
	@echo "hello world"

install:
	@echo "Installing project dependencies using Poetry..."
	poetry install

server:
	@echo "Server starting..."
	poetry run python3 main.py
