#!/bin/bash

# Poetry is must for this script
read -p "Do you have poetry installed? (y/n)" poetry_yn

if [[ $poetry_yn == "y" || $poetry_yn == "Y" ]] then
	# install poetry deps
	echo "Installing project dependencies using Poetry..."
	poetry install

	while true; do
		read -p "Do you want to start server? (y/n)" start_yn

		case $start_yn in
			[Yy]* )
				echo "Server starting...";
				poetry run dev;;

			[Nn]* )
				echo "Exiting...";
				echo "you can run server later using the command:";
				echo "poetry run dev";
				exit;;
			* ) echo "Please answer with Y/y/N/n.";;

		esac
	done

else
	echo "Sorry, this script only works with poetry";
	echo "Please install it and re-run this script";
	exit;
fi
