from fastapi import FastAPI
from consumer import Consumer

# Create FastAPI app and Consumer instance
app = FastAPI()
consumer = Consumer(topic="not_interesting", server_address="localhost:9092")

# return the consumed data from the topic "not_interesting"
@app.get("/")
def consume_data():
    try:
        consumer.consume()
        return {"status": "Data consumption started"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}