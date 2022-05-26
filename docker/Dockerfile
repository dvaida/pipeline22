FROM python:3.9-slim-buster

RUN mkdir /app
COPY requirements.txt /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY *.py /app

ENV PORT=8080
ENV TREE="pine"
CMD ["sh", "-c", "uvicorn service:app --port $PORT --host 0.0.0.0"]
