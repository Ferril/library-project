FROM python:3.7

ARG APP_ENV

ENV DJANGO_ENV=${APP_ENV}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=0.12.11

RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /library
COPY ./poetry.lock pyproject.toml /library/

RUN poetry config settings.virtualenvs.create false \
  && poetry install $(test "$DJANGO_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY ./entrypoint.sh /library/entrypoint.sh

COPY . /library

ENTRYPOINT ["/library/entrypoint.sh"]