docker: 
	docker build -t string-encoder .

run:
	docker-compose up -d

run-client:
	docker exec -it string-encoder bash -c "nameko shell --config /var/nameko/conf.yml"

stop:
	docker-compose down

re-run: docker run