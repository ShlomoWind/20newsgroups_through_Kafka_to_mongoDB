FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY consumer.py .
COPY not_interesting_server.py .
EXPOSE 8003
CMD ["uvicorn", "not_interesting_server:app", "--host", "0.0.0.0", "--port", "8003"]