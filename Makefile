docker-run:
	docker-compose run --rm worker $(cmd)

init:
	@make --no-print-directory start wait init-db

init-db:
	@make --no-print-directory docker-run cmd="python scripts/init_db.py"

start:
	docker-compose up -d

stop:
	docker-compose stop

wait:
	sleep 20