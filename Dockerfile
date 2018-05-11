FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project

RUN apk update && \
apk add --virtual build-deps gcc python3-dev musl-dev && \
apk add postgresql-dev

ADD requirements.txt /project/
RUN pip3 install -r requirements.txt

RUN apk add --update bash && rm -rf /var/cache/apk/*
ADD . /project/

WORKDIR /project/src
#CMD python3 manage.py makemigrations && python3 manage.py migrate
#CMD gunicorn core.wsgi:application -w 2 -b :8001

#RUN pip install pipenv
#RUN pipenv install --system
#EXPOSE 8000