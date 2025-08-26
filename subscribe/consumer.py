from kafka import KafkaConsumer
from pymongo import MongoClient
from datetime import datetime, timezone

mongo_url = "mongodb://localhost:27017/"
db_name = "news_db"

# Receives server address and topic in constructor and creates a consumer instance
class Consumer:
    def __init__(self,topic,server_address):
        self.topic = topic
        self.server_address = server_address
        self.consumer = KafkaConsumer(self.topic,
                                      group_id= self.topic,
                                      bootstrap_servers=[self.server_address],
                                      value_deserializer=lambda x: x.decode('utf-8'),
                                      consumer_timeout_ms=10000)
        self.mongo_client = MongoClient(mongo_url)
        self.db = self.mongo_client[db_name]
        self.collection = self.db[self.topic]

# Consumes messages from the topic
    def consume(self):
        for message in self.consumer:
            data = {
                "message": message.value,
                "timestamp": datetime.now(timezone.utc)
            }
            self.collection.insert_one(data)
            print(f"Consumed message: {message.value} from topic: {self.topic}")

# Closes the consumer instance
    def close(self):
        self.consumer.close()
        self.mongo_client.close()