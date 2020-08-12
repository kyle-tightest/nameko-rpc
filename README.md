# nameko-rpc

This is a microservice project that uses the [Nameko](https://github.com/nameko/nameko) framework.  
The following microservices are available:  
- [Square Odd Integers](square-odd-integers/README.md)
- [String Encoder](string-encoder/README.md)

Please read [this](Research.md) for more information on how this project was implemented and the relevant design decisions that were made.

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

Build the docker images for the microservices:
```bash
make docker
```

If you do not have `make` installed, execute [this](Makefile#L2-L3) command instead. 

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

If you do not have `make` installed, execute [this](Makefile#L8) command instead.

In this shell, you can test a client-side call to `square_odd_service` (Square Odd Integers) as well as the `string_encoder_service` (String Encoder):
```bash
>>> n.rpc.square_odd_service.square([1,2,3])
'[1, 2, 9]'
>>> n.rpc.string_encoder_service.encode(["Hello", "Invictus"])
{'Hello': 'POlJzw==', 'Invictus': '+AzuxBhP'}
```

