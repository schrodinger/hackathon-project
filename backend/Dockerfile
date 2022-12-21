FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=api.settings.settings


WORKDIR /app

RUN mkdir -p /var/log/gunicorn

EXPOSE 8000

COPY requirements.txt setup.py run.sh ./
COPY api ./api

COPY science ./science
RUN pip install -r requirements.txt
RUN apt-get update &&  apt-get install ffmpeg libsm6 libxext6  -y
#TODO see if we can cut down on the number of installs above

ENTRYPOINT ["/bin/bash", "run.sh"]
