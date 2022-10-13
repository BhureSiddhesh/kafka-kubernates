from datetime import time

from confluent_kafka import Consumer

print("Starting Kafka Consumer")



conf = {
    'bootstrap.servers' : 'localhost:9092',
    'group.id' : '0',

}

print("connecting to Kafka topic")

consumer = Consumer(conf)

consumer.subscribe(['sample-topic'])
print('connected..')
while True:
    msg = consumer.poll(1.0)


    if msg is None:
        continue
    if msg.error():
        print("Consumer error happened: {}".format(msg.error()))
        continue
    print("Connected to Topic: {} and Partition : {}".format(msg.topic(), msg.partition() ))
    # print("Received Message : {} with Offset : {}".format(msg.value().decode('utf-8'), msg.offset() ))
    dict = eval(msg.value().decode('utf-8'))
    print(dict['message'])

#consumer.close()