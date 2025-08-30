env:
	cp .env.example .env

db:
	docker-compose up -d

req:
	pip install -r requirements.txt

upgrade:
	alembic upgrade head
