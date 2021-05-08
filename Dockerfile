FROM python:3.9-slim

ENV LOG_LEVEL=INFO

COPY src /app


RUN apt-get update \
     && apt-get upgrade -y \
     && apt-get clean

RUN python -m pip install --upgrade pip setuptools

ENTRYPOINT ["python", "/app/authorize.py"]