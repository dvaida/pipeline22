FROM python:3.9-slim-buster

RUN mkdir /app
COPY requirements.txt /app
COPY *.py /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV PORT=8080
CMD ["uvicorn", "service:app", "--port", "8080", "--host", "0.0.0.0"]