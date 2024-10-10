up:
	@echo "Starting django service ..."
	python manage.py runserver

migrate:
	@echo "Make migrations & migrate & start project ..."
	python manage.py makemigrations && python manage.py migrate && python manage.py runserver

migrate_t:
	@echo "Make migrations for text_handler ..."
	python manage.py makemigrations text_handler