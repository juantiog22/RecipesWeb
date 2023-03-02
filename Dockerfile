# Dockerfile
FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app  
COPY . /app
RUN pip install -r requirements.txt
