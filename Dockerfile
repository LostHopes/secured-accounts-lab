FROM python:latest

WORKDIR /app

ENV VIRTUAL_ENV=/app/.env
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY pyproject.toml poetry.lock /app/

RUN pip install --upgrade pip \
    && pip install poetry \
    && python -m venv $VIRTUAL_ENV \
    && poetry config virtualenvs.path "$VIRTUAL_ENV" \
    && poetry install --without dev

COPY . /app/

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "src/run.py" ]