FROM python:3.7-alpine
LABEL maintainer="Bara Ramadhan bararamadhan@gmail.com"

ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip && pip install rq-dashboard

EXPOSE 9181

CMD ["rq-dashboard"]