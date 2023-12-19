FROM python:3.9.7-slim AS builder

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9.7-slim

WORKDIR /app

COPY --from=builder /app /app

COPY . .

# Cleanup
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

ENV FLASK_ENV=production

USER nobody

CMD ["python", "main.py"]
