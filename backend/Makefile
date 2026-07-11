run:
	uvicorn app.main:app --reload

test:
	pytest

migrate:
	alembic upgrade head

makemigration:
	alembic revision --autogenerate -m "$(m)"

redis:
	redis-server

docker-up:
	docker compose up -d

docker-down:
	docker compose down
