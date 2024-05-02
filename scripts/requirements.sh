#!/bin/bash

# Poetry is must for this script
read -p "Do you have poetry installed? (y/n): " poetry_yn

if [[ $poetry_yn == "y" || $poetry_yn == "Y" ]] then
	# install poetry deps
	echo "Exporting poetry dependencies to requirements.txt"
	poetry run pip freeze > requirements.txt
	exit 0

else
	echo "Sorry, this script only works with poetry"
	echo "Please install it and re-run this script"
	exit 0
fi
