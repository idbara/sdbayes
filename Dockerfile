FROM python:3.7-alpine
LABEL maintainer="Bara Ramadhan bararamadhan@gmail.com"

# set work directory
WORKDIR /usr/src/run

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/run/requirements.txt
RUN apk --update add --no-cache postgresql-client
RUN apk --update add --no-cache netcat-openbsd
RUN apk --update add --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN apk --update add --no-cache libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk --update add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN apk add --update --no-cache tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime && \
    echo "Asia/Jakarta" > /etc/timezone && \
    date && \
    rm -fr /tmp/* /var/cache/apk/*

# install requirements
RUN pip install --upgrade pip && pip install --default-timeout=100 future && \
    pip install -r requirements.txt

# set working directory
COPY . /usr/src/run
RUN chmod +x /usr/src/run/entrypoint.prod.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/run/entrypoint.prod.sh"]
