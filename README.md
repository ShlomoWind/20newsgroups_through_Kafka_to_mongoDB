# 20 Newsgroups Dataset Processing Pipeline

A real-time data pipeline that processes the famous 20 Newsgroups dataset through Apache Kafka and stores the results in MongoDB. This project demonstrates event-driven architecture patterns for text data processing and storage.

## Overview

This project implements a complete data pipeline that:
- Loads the 20 Newsgroups dataset
- Streams the data through Apache Kafka for real-time processing
- Stores processed documents in MongoDB for efficient querying and analysis

The 20 Newsgroups dataset is a collection of approximately 20,000 newsgroup documents, partitioned across 20 different newsgroups, making it ideal for text classification and natural language processing tasks.

## Architecture

```
[20 Newsgroups Dataset] → [Kafka Producer] → [Kafka Topic] → [Kafka Consumer] → [MongoDB]
```

## Features

- **Real-time streaming**: Process newsgroup messages as they flow through Kafka
- **Scalable architecture**: Kafka ensures high throughput and fault tolerance
- **Flexible storage**: MongoDB provides document-based storage for text data
- **Data preprocessing**: Clean and structure newsgroup messages
- **Monitoring**: Track pipeline performance and data flow

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ShlomoWind/20newsgroups_through_Kafka_to_mongoDB.git
cd 20newsgroups_through_Kafka_to_mongoDB
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Kafka and MongoDB services

### 4. Use Docker Compose
```bash
docker-compose up -d --build
```
## Project Structure

```
20newsgroups_through_Kafka_to_mongoDB/

├── publish/
│   ├── data_loader.py      
│   ├── publisher_server.py 
│   ├── Dockerfile         
│   ├── requirements.txt   
│   └── publisher.py        
├── subscribe/    
│   ├── consumer.py
│   ├── interesting_server.py
│   ├── not_interesting_server.py
│   ├── not_interesting.Dockerfile
│   ├── interesting.Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```
## 📞 Contact

**שלמה ווינד (Shlomo Wind)**
- GitHub: [@ShlomoWind](https://github.com/ShlomoWind)
- Project Link: [https://github.com/ShlomoWind/20newsgroups_through_Kafka_to_mongoDB](https://github.com/ShlomoWind/20newsgroups_through_Kafka_to_mongoDB)

---

⭐ If this project helped you, please give it a star on GitHub!