FROM python:3.11-slim

COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

WORKDIR /app
EXPOSE 5000

ENTRYPOINT ["python", "app.py"]