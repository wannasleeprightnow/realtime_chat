DC = sudo docker compose

restart_all: drop_all start_all

start_all:
	$(DC) up --build -d

drop_all:
	$(DC) down

logs_all:
	$(DC) logs -f