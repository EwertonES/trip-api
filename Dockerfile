FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

COPY app/ /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --timeout 0 main:app