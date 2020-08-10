# String Encoder

This rpc service implements the Nameko hello world example.

## Minimum requirements to run
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Full requirements (for development)
- [Python 3](https://www.python.org/downloads/)
- [Nameko](https://github.com/nameko/nameko)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Pipenv (for package management)](https://pypi.org/project/pipenv/)
- [Make (for convenience)](https://www.gnu.org/software/make/manual/make.html)

## Setup

Build the docker image for square-odd-integers:
```bash
make docker
```

If you do not have `make` installed, execute [this](Makefile#L2 command instead. 

## Run

Run the service using Docker-compose:
```
make run
```

If you do not have `make` installed, execute [this](Makefile#L5) command instead.

## Test

Run a client using the nameko shell:
```
make run-client
```

If you do not have `make` installed, execute [this](Makefile#L5) command instead.

In this shell, you can test a client-side call:
```bash
>>> n.rpc.greeting_service.hello(name="Invictus")
'Hello, Invictus'
```