FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app
WORKDIR /app
CMD ["uv", "run", "./main.py"]
