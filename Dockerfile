# Base image
FROM python:3.10-bullseye

RUN pip install peewee psycopg2-binary

ENV PYTHONPATH "${PYTHONPATH}:/code"