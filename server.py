from fastapi import FastAPI
from data_loader import Data
from publisher import Producer
import uvicorn

app = FastAPI()
data = Data()
producer = Producer("localhost:9092")

@app.get("/")
def publish_data():
    try:
        interesting_batch, not_interesting_batch = data.get_data()
        for message in interesting_batch:
            producer.publish(message, topic="interesting")
        for message in not_interesting_batch:
            producer.publish(message, topic="not_interesting")
        return {"status": "Data published"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}