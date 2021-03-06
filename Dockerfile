FROM python:3.7-buster
LABEL maintainer="Bara Ramadhan bararamadhan@gmail.com"

# set work directory
WORKDIR /usr/src/app

# set working directory
COPY . /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/run/requirements.txt
RUN apt-get update && apt-get install -y postgresql-client netcat-openbsd gcc libc-dev libxml2-dev libxslt-dev libffi-dev gcc musl-dev curl tk-dev tcl-dev

# install requirements
RUN pip install --upgrade pip && pip install --default-timeout=100 future && \
    pip install -r requirements.txt


RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
