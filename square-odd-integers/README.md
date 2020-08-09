# Square Odd Integers

This service implements the Nameko Hello World example.  

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Nameko](https://github.com/nameko/nameko)
- [Docker](https://docs.docker.com/get-docker/)
- [RabbitMQ 3 Docker image](https://hub.docker.com/_/rabbitmq)
- [Pipenv (for package management)](https://pypi.org/project/pipenv/)
- [Make (for convenience)](https://www.gnu.org/software/make/manual/make.html)

## Setup

Install dependent packages with `pipenv`:
```
pipenv install
```

Activate Python environment:
```
pipenv shell
```

## Run

A Makefile was added to this microservice for convenience.   

How to run:
```bash
make run
```

While its running, open a seperate terminal to test a client-side call:
```bash
nameko shell
>>> n.rpc.greeting_service.hello(name="Invictus")
'Hello, Invictus'

```
How to stop:
```bash
make stop
```

How to exit the Python environment (within the shell):
```
exit
```
