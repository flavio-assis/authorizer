FROM python:3.9-slim

ENV LOG_LEVEL=INFO
ENV VERSION='0.0.1'

COPY . /authorizer

WORKDIR /authorizer

RUN apt-get update \
     && apt-get upgrade -y \
     && apt-get clean

RUN python setup.py sdist
RUN python -m pip install --upgrade pip setuptools dist/authorizer-${VERSION}.tar.gz


ENTRYPOINT ["authorize"]