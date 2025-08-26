import os

from fastapi import FastAPI
from consumer import Consumer

address = os.getenv("KAFKA_BROKER", "localhost:9092")
topic = "not_interesting"

# Create FastAPI app and Consumer instance
app = FastAPI()
consumer = Consumer(topic=topic, server_address=address)

# return the consumed data from the topic "not_interesting"
@app.get("/")
def consume_data():
    try:
        consumer.consume()
        return {"status": "Data consumption started"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}