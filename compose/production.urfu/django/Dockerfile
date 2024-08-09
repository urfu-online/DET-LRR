FROM node:16-bullseye-slim as client-builder

WORKDIR /app
COPY ./package.json /app
RUN npm install && npm cache clean --force
COPY . /app
RUN npm run build

# Python build stage
FROM python:3.10-slim-bullseye as base

ENV TZ 'Asia/Yekaterinburg'
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y upgrade \
    && echo $TZ > /etc/timezone  \
    && apt-get install -y tzdata \
    && rm /etc/localtime  \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  \
    && dpkg-reconfigure -f noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

ENV LC_ALL ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements /requirements
RUN apt-get update \
    && apt-get install -y --no-install-recommends locales locales-all localepurge\
    && dpkg-reconfigure -f noninteractive locales && localepurge \
    && apt-get update && apt-get install -y --no-install-recommends build-essential pkg-config gettext git curl graphviz libgraphviz-dev libpq-dev poppler-utils poppler-utils libmagic-dev  \
    zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev \
    && pip install --upgrade --no-cache-dir pip \
    && pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements \
    && apt-get remove -y build-essential pkg-config localepurge \
    && rm -rf /var/lib/apt/lists/*

#RUN addgroup --system django \
#    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.

COPY ./compose/production.urfu/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY ./compose/production.urfu/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/production.urfu/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker


COPY ./compose/production.urfu/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat


# COPY ./compose/production.urfu/django/celery/flower/start /start-flower
# RUN sed -i 's/\r$//g' /start-flower
# RUN chmod +x /start-flower

COPY --from=client-builder /app /app
# --chown=django:django
#USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
