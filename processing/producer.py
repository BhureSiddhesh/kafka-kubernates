from uuid import uuid4

from confluent_kafka import Producer

jsonString1 = """ {'name':'Gal', 'email':'Gadot84@gmail.com', 'contact': '899898656','message':'hello I am siddhesh Bhure and this is my message'} """
jsonString2 = """ {'name':'siddhesh', 'email':'siddheshbhure@outlook.com', 'contact': '899898656','message':'this is my message'} """

dict = {'name':'yee','yes':'one'}

kafka_topic_name = "sample-topic"

print("Starting Kafka Producer")
conf = {
    'bootstrap.servers': 'localhost:9092'
}

print("connecting to Kafka topic...")
producer1 = Producer(conf)

producer1.poll(0)

try:

    producer1.produce(topic=kafka_topic_name, key=str(uuid4()), value=jsonString1.encode())
    producer1.produce(topic=kafka_topic_name, key=str(uuid4()), value=jsonString2.encode())

    producer1.flush()

except Exception as ex:
    print("Exception happened :", ex)

print("\n Stopping Kafka Producer")
