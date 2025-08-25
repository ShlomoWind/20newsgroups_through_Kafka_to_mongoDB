from kafka import KafkaProducer

# Receives server address and topic in constructor and crates a producer instance
class Producer:
    def __init__(self,topic,server_address):
        self.topic = topic
        self.server_address = server_address
        self.producer = KafkaProducer(bootstrap_servers=[self.server_address],
                                      value_serializer=lambda x: x.encode('utf-8'))

# Publishes message to the topic
    def publish(self,message):
        self.producer.send(self.topic, value=message)
        self.producer.flush()
        print(f"Published message: {message} to topic: {self.topic}")

# Closes the producer instance
    def close(self):
        self.producer.close()