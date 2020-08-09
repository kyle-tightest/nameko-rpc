Research steps followed for this project:

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