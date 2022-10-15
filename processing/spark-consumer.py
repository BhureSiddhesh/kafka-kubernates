from datetime import time

from confluent_kafka import Consumer
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext


def spark_context_creator():
    print('inside spark')
    conf = SparkConf()
    # set name for our app
    conf.setAppName("KafkaSparkStreaming")
    # The master URL to connect
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


# sc = spark_context_creator()
# print('spark-started')
consumer = connect_kafka('localhost:19092', 'crypto-ETH-topic')

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error happened: {}".format(msg.error()))
        continue

    dict = eval(msg.value().decode('utf-8'))
    print(dict)

consumer.close()
