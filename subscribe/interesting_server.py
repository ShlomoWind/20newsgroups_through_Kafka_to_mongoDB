from fastapi import FastAPI
from subscribe.consumer import Consumer

address = "localhost:9092"
topic = "interesting"

# Create FastAPI app and Consumer instance
app = FastAPI()
consumer = Consumer(topic=topic, server_address=address)

# return the consumed data from the topic "interesting"
@app.get("/")
def consume_data():
    try:
        consumer.consume()
        return {"status": "Data consumption started"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8005)