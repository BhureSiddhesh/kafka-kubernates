from uuid import uuid4

import websocket
import json

from confluent_kafka import Producer


def open_conn(ws):
    subscribe = {
        "type": "subscribe",
        "product_ids": ["ETH-EUR"],
        "channels": ["ticker"]
    }
    print('inside')
    try:
        ws.send(json.dumps(subscribe))
    except Exception as e:
        print(e)
    print('socket open')


def show_message(ws, message):

    producer1.produce(topic=kafka_topic_name, key=str(uuid4()), value=message.encode())
    producer1.flush(5)
    print(message)


coinbase_socket = 'wss://ws-feed.exchange.coinbase.com'

try:
    print("Starting Kafka Producer")
    conf = {
        'bootstrap.servers': 'localhost:9092'
    }
    kafka_topic_name = "crypto-ETH-topic"
    print("connecting to Kafka topic...")
    producer1 = Producer(conf)
    ws = websocket.WebSocketApp(coinbase_socket, on_open=open_conn, on_message=show_message)
    ws.run_forever()
except Exception as e:
    print(e)
