FROM python:latest

WORKDIR /app

ENV VIRTUAL_ENV=/app/.env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY pyproject.toml poetry.lock /app/

RUN python -m venv $VIRTUAL_ENV && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.path "$VIRTUAL_ENV" && \
    poetry install --without dev

COPY . /app/

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "src/run.py" ]