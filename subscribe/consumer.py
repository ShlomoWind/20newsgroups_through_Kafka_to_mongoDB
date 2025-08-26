from kafka import KafkaConsumer

# Receives server address and topic in constructor and creates a consumer instance
class Consumer:
    def __init__(self,topic,server_address):
        self.topic = topic
        self.server_address = server_address
        self.consumer = KafkaConsumer(self.topic,
                                      bootstrap_servers=[self.server_address],
                                      value_deserializer=lambda x: x.decode('utf-8'))

# Consumes messages from the topic
    def consume(self):
        for message in self.consumer:
            print(f"Consumed message: {message.value} from topic: {self.topic}")

# Closes the consumer instance
    def close(self):
        self.consumer.close()