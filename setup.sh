#!/bin/bash

# Poetry is must for this script
read -p "Do you have poetry installed? (y/n): " poetry_yn

if [[ $poetry_yn == "y" || $poetry_yn == "Y" ]] then
	# install poetry deps
	echo "Installing project dependencies using Poetry..."
	poetry install

	read -p "Do you want to start server? (y/n): " start_yn

	case $start_yn in
		[Yy]* )
			echo "Server starting..."
			poetry run fastapi dev main.py;;

		[Nn]* )
			echo "Exiting..."
			echo "you can run server later using the command:"
			echo "poetry run dev"
			exit;;
		* ) exit 0

	esac

else
	echo "Sorry, this script only works with poetry"
	echo "Please install it and re-run this script"
	exit 0
fi
