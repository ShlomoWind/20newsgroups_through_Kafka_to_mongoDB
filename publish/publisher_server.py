from fastapi import FastAPI
from publish.data_loader import Data
from publish.publisher import Producer
import uvicorn

address = "localhost:9092"
topic_1 = "interesting"
topic_2 = "not_interesting"

# Create FastAPI app, Data loader and Producer instance
app = FastAPI()
data = Data()
producer = Producer(address)

# publish interesting and not interesting data by topic
@app.get("/")
def publish_data():
    try:
        interesting_batch, not_interesting_batch = data.get_data()
        for message in interesting_batch:
            producer.publish(message, topic=topic_1)
        for message in not_interesting_batch:
            producer.publish(message, topic=topic_2)
        return {"status": "Data published"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8003)