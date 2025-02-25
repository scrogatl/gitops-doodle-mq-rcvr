FROM python:3.10-slim-bullseye 
# FROM python:3.10

WORKDIR /mq-rcvr

COPY src/requirements.txt /mq-rcvr/requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV NEW_RELIC_APP_NAME=doodle-mq-rcvr
ENV PYTHONUNBUFFERED=1

COPY src/app.py /mq-rcvr
# CMD python app.py
CMD newrelic-admin run-program python app.py
