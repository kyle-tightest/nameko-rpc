FROM python:3.8-slim
RUN pip install pipenv

COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

# See: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
RUN addgroup --gid 2000 nameko && \
  adduser --system --uid 2000 --ingroup nameko nameko

RUN mkdir /var/nameko

USER nameko:nameko

WORKDIR /var/nameko/
COPY server.py .
COPY conf.yml .

EXPOSE 8000

CMD ["nameko", "run", "--config", "/var/nameko/conf.yml", "server"]