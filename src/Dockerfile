FROM python:3.11

WORKDIR /app

COPY ./requirements.txt .

RUN apt-get update && \
    apt-get install -y netcat-traditional

RUN pip install --upgrade pip && \
    pip install --no-cache-dir poetry==1.4.2 && \
    poetry config virtualenvs.create false

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install --without dev

# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt --no-cache-dir

COPY . .
