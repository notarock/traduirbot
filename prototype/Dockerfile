FROM python:3.8-slim

WORKDIR /app

RUN pip install pipenv
COPY Pipfile.lock .
RUN pipenv sync --bare

COPY . .

RUN ls -l

CMD pipenv run python3 src/server.py
