run-rabbitmq:
	docker run --rm --name rabbitMQ -d -p 5672:5672 rabbitmq:3

run-nameko-service:
	@echo "RabbitMQ will take some time to startup, so ignore the first few connection failures."
	nameko run server

echo-warning:
	@echo "RabbitMQ will take some time to startup, so ignore the first few connection failures."

run: run-rabbitmq run-nameko-service

stop-rabbitmq:
	docker stop rabbitMQ

stop: stop-rabbitmq