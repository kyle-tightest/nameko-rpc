Research steps followed for this project:

# Overall strategy and layout
- The business logic mentioned in the requirements did not seem too difficult. So I decided to tackle the environment and setup first, before looking at the business logic.
- The numbered headings below enumerate the seperate commits made to this repository.
- I followed the principle of having working and well documented steps at each commit. Even though this may take longer to implement, it provides clear direction to anyone reading this repository (including myself) and gives explanation to any design decisions and why they might have changed between commits. 

# 1. Implement Square Odd Integers as a Nameko Hello World example

- Read the project brief.
- Read up on PyPy.
  - A faster version of Python due to using a Just-In-Time compiler instead of a interpreter.
  - This is similar to the JVM (Java), where compiled code (bytecode) has to be interpreted to machine code. The JVM then compiles bytecode to machine during runtime, so that it does not have to translate each time. Compilation to machine takes time and resources, so the decision of where and when to do this varies. Java has run parameters (eg. `-client` and `server`) that change this behaviour, and different Java runtimes also do this differently (eg. [HotSpot](https://en.wikipedia.org/wiki/HotSpot) and [GraalVM](https://en.wikipedia.org/wiki/GraalVM).  
  - For this project, I don't think execution time is that important. So I decided to use ordinary interpreted Python (also known as [CPython](https://en.wikipedia.org/wiki/CPython)).
- Read up on package management in Python.
  - I've used Python with a requirements.txt file before. Not the best experience. Virtual environments have to be created for each project, and the user has to switch between them to run things.
  - I found [Pipenv](https://pypi.org/project/pipenv/) which seemed to be a good alternative. A user-friendly combination of `pip` and `virtualenv`.  
- Read the [Nameko repo](https://github.com/nameko/nameko) and some of the accompanying [documentation](https://nameko.readthedocs.io/en/stable/what_is_nameko.html#when-should-i-use-nameko).  
  - It mentioned that I had to run RabbitMQ.
  - Read up a little on RabbitMQ and saw how it works (Hello World tutorial).
  - Read up on AMPQ and got a gist of the main terminology: Broker, Message, Consumer and Producer (sometimes called Publisher).
  - Ran RabbitMQ in Docker.
- Implemented the Square Odd Integers service as a Nameko Hello World example for an initial working prototype.

# 2. Dockerise Square Odd Integers

- Searched for a Docker base image for a Nameko service.
  - Only thing I could find by Nameko was an [examples repo](https://github.com/nameko/nameko-examples).
  - The docs explain the examples but not really what the Docker base is made of for these examples. This is more clear when looking at the individual Dockerfiles which follow a similar structure.
  - The examples make use of [multistage Docker builds](https://docs.docker.com/develop/develop-images/multistage-build/), which allows for using one image only for building and another only for deploying. This can save on space when your deployment image does not have all the build tools needed for building. It is also more secure, only using what is needed for deployment.
  - However, the structure didn't make enough sense to me for this project. The base image used `nameko-example-base` was also not publically available so I could not be sure what I was running.
  - I decided to go with a `python:3.8-slim` base image and install `pip` to get all the packages required.
  - I converted the Pipfile to `requirements.txt` (in the Docker build) in order to just use `pip` and not need `pipenv` in the docker container as well.
- Thought about how to run the Docker container/s.
  - I decided to use [Docker Compose](https://docs.docker.com/compose/install/) for running containers.
    - The current nameko service (and possibly others in future) depends on a running Rabbit MQ. Docker Compose easily resolves dependent services.
    - I want to run the docker container with a convenient name that makes it easier to work with. This can be set in the docker-compose file.
    - The services will run in their own Docker network (default docker-compose [network mode](https://docs.docker.com/compose/networking/#configure-the-default-network)). This will make sure that it doesn't interfere with anything else running on the user's PC.
  - I had to create a `conf.yml` file in order to tell the Nameko service how to talk to RabbitMQ (using the docker service name as a hostname).
- Now the user only needs `Docker` and `Docker Compose` to run the service. 
- Added a convenient `make` command to test a client connection.

# 3. Implement Square Odd Integers business logic

- Did not do any research at this step, the business logic was pretty straight forward.
- Added a make command to conveniently rebuild the docker image and re-run.

# 4. Implement String Encoder as Nameko Hello World example

- The String Encoder service is first implemented as a hello world example.
  - A seperate service from Square Odd Integers. This follows a [Domain Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) architecture for microservices.
  - It will reside in a new folder in the root directory.
  - Many building blocks can be copied (and possibly slightly edited) from Square Odd Integers, eg. Pipfile, Dockerfile, etc.
- However, seperating the two Docker Compose services will mean two seperate services in two seperate Docker networks.
  - Two RabbitMQ services is unneccesary, unless you want to scale.
  - This makes a little bit more complicated to run and test the different services. Especially if these services form part of one product and need to deployed together.
  - But it is also important to give the user to test them seperately if needed. Seperation of concerns, eg. a bug was found on Sqaure Odd Integers and someone with little context needs to be fix it. They should not need to worry about String Encoder as well.
- Thus, I created another Docker Compose file to run them both simultaneously.
  - The Docker Compose files to run them individually are still there.
- Added appropriate `Make` commands to allow the user to quickly run both services.

# 5. Implement String Encoder business logic

- Read up on [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding).
  - Algorithm for lossless data compression.
  - The input is an alphabet (string of characters) and the probability of each character occuring in the string (which could also be calculated on the fly for a given string).
  - The output is a binary string representing the compressed input.
  - The compressed string can then be decompressed if you have the binary tree used to compress it.
  - Thus, the compressor and decompressor must have access to the same binary tree or be able to reconstruct it exactly.
- I found a PyPI library which does huffman encoding and decoding called [dahuffman])(https://pypi.org/project/dahuffman/)
  - Usage example is straight-forward.
  - Built for Python 3.5 and up
  - Only uses standard Python libraries (no external dependency risk)
  - Developed on in the last 2 months
- The huffman encoder will be trained (input alphabet) with data from [Shakespear's complete works](http://www.gutenberg.org/files/100/100-0.txt) on startup.
  - Conveninetly provided by the library
- The resulting byte array (binary tree) will be base64 encoded and decoded before returning to the user.