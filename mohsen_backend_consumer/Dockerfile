FROM python:3.8
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
COPY /wait-for-it.sh /usr/local
COPY ./requirements.txt /requirements.txt
RUN echo "y" | apt-get update
RUN echo "y" | apt-get upgrade
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app
COPY /app /app/