FROM python:3.12-slim

RUN pip install --no-cache-dir poetry

COPY . ./new_poj

WORKDIR /new_poj

RUN poetry install --no-root
