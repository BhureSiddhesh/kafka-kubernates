import uuid
from datetime import time
from elasticsearch import Elasticsearch
from confluent_kafka import Consumer


def connect_elastc():
    es = Elasticsearch("http://elastic:elastic@localhost:9200",)

    return es


def connect_kafka_consumer():
    print("Starting Kafka Consumer")

    conf = {
        'bootstrap.servers': 'localhost:19092',
        'group.id': '0',

    }
    print("connecting to Kafka topic")

    consumer = Consumer(conf)
    return consumer


elastic = connect_elastc()
consumer = connect_kafka_consumer()

consumer.subscribe(['crypto-ETH-topic'])
print('connected..')
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error happened: {}".format(msg.error()))
        continue

    dict = eval(msg.value().decode('utf-8'))
    if dict['type'] == 'ticker':
        elastic.index(index= "crypto-index" , body = dict)
        print(dict)
