# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

# Set env
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Run as non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
