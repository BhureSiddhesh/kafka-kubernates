from datetime import time

from confluent_kafka import Consumer

print("Starting Kafka Consumer")

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': '0',

}

print("connecting to Kafka topic")

consumer = Consumer(conf)

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
    print(dict)


