app:
	@echo "Starting django service ..."
	cd src && python manage.py runserver

migrate:
	@echo "Make migrations & migrate & start project ..."
	cd src && python manage.py makemigrations && python manage.py migrate && python manage.py runserver

migrate_t:
	@echo "Make migrations for text_handler ..."
	cd src && python manage.py makemigrations text_handler

up:
	@echo "Starting docker container ..."
	sudo docker compose up --build

restart:
	@echo "Deleting and starting docker container ..."
	sudo docker compose stop && docker rm && docker compose up