FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

COPY *.py /app/
COPY requirements.txt /app/

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD = ['unicorn', 'server.app', '--reload', '--host', '0.0.0.0', '--port'. '80']