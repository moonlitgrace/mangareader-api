#!/bin/bash

VENV = "venv"

# create venv if its not created
if [! -d "${VENV}"]; then
	echo "Creating virtual environment..."
	python3 -m venv "${VENV}"
fi

# activate venv
source "${VENV}"/bin/activate

# install poetry deps
echo "Installing project dependencies using Poetry..."
poetry install