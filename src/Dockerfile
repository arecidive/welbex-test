FROM python:3.11-alpine3.19

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /temp/requirements.txt
COPY . /src
WORKDIR /src
EXPOSE 8000

RUN pip install -r /temp/requirements.txt