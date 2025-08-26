from kafka import KafkaProducer

# Receives server address and topic in constructor and crates a producer instance
class Producer:
    def __init__(self,server_address):
        self.server_address = server_address
        self.producer = KafkaProducer(bootstrap_servers=[self.server_address],
                                      value_serializer=lambda x: x.encode('utf-8'))

# Publishes message to the topic
    def publish(self,message,topic):
        self.producer.send(topic, value=message)
        self.producer.flush()
        print(f"Published message: {message} to topic: {topic}")

# Closes the producer instance
    def close(self):
        self.producer.close()