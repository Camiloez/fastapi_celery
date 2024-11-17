FROM python:3.11

RUN pip install poetry==1.8.3

WORKDIR /usr/src/app

copy pyproject.toml poetry.lock .

RUN poetry install --no-root 

COPY . .

