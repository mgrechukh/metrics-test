# syntax=docker/dockerfile:experimental
FROM alpine:3.11
ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
RUN apk add --update py2-pip

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk add curl
ADD app.py /src/
WORKDIR /src
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
