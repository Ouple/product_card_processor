FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=120 --retries=10 --progress-bar off -r requirements.txt

COPY app ./app

CMD ["python", "-m", "app.cli", "--help"]