from datetime import time
import ast
from confluent_kafka import Consumer
from elasticsearch import Elasticsearch
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

from pyspark.streaming import StreamingContext


def connect_elastc():
    es = Elasticsearch("http://elastic:elastic@localhost:9200")
    return es


def spark_context_creator():
    print('inside spark')
    conf = SparkConf()
    conf.setAppName("KafkaSparkStreaming")
    conf.setMaster('spark://127.0.0.1:7077')
    sc = None
    try:
        sc.stop()
        sc = SparkContext(conf=conf)
    except:
        sc = SparkContext(conf=conf)
    return sc


def connect_kafka(server_name, topic_name):
    print("Starting Kafka Consumer")
    conf = {
        'bootstrap.servers': server_name,
        'group.id': '0',
    }
    print("connecting to Kafka topic")
    consumer = Consumer(conf)

    consumer.subscribe([topic_name])
    print('connected..')
    return consumer


sc = spark_context_creator()
print('spark-started')
elastic = connect_elastc()
consumer = connect_kafka('localhost:19092', 'airline-tweet-topic')

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error happened: {}".format(msg.error()))
        continue

    # for handling emojis in tweets
    message = msg.value().decode('utf-16')
    print(message)
    try:
        dict = eval(message)
        elastic.index(index="tweet-index", body=dict)
        print(dict)

    except Exception as e:
        print(e)


consumer.close()
