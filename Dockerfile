FROM python:3.9

RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1s

# project variables
ENV PORT=8000
ARG SETTINGS=production
ENV SETTINGS_STRING="--settings=urlshortener.settings.$SETTINGS"

# install environment dependencies
RUN pip3 install --upgrade pip

# Install requirements
RUN pip install -r requirements.txt

EXPOSE $PORT
RUN python manage.py makemigrations $SETTINGS_STRING
RUN python manage.py migrate $SETTINGS_STRING
CMD python manage.py runserver 0.0.0.0:$PORT $SETTINGS_STRING