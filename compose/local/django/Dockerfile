FROM python:3.10-slim-bullseye

ENV LC_ALL ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ 'Asia/Yekaterinburg'
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y --no-install-recommends build-essential apt-utils wget gnupg2 lsb-release \
    && apt-key adv --fetch-keys https://www.postgresql.org/media/keys/ACCC4CF8.asc  \
    && echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && apt-get update \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev postgresql-client-12 \
  # Translations dependencies
  && apt-get install -y --no-install-recommends  gettext \
  && apt-get install -y --no-install-recommends graphviz libgraphviz-dev pkg-config git \
  && apt-get install -y --no-install-recommends zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev libopenjp2-7-dev poppler-utils libmagic-dev \
  # cleaning up unused files
  #&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements

RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r /requirements/local.txt

#RUN apt-get remove -y perl \
    #&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

COPY ./compose/production.urfu/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

# COPY ./compose/local/django/celery/flower/start /start-flower
# RUN sed -i 's/\r$//g' /start-flower
# RUN chmod +x /start-flower

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
