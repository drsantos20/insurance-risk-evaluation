.PHONY: test
test:
	docker-compose exec web pytest .

.PHONY: start
start:
	docker-compose up -d --build
