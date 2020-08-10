docker: 
	docker build -t square-odd-integers ./square-odd-integers
	docker build -t string-encoder ./string-encoder

run:
	docker-compose up -d

run-client:
	docker exec -it square-odd-integers bash -c "nameko shell --config /var/nameko/conf.yml"

stop:
	docker-compose down

re-run: docker run