import json
from uuid import uuid4
from confluent_kafka import Producer
import pandas as pd

kafka_topic_name = "airline-tweet-topic"

print("Starting Kafka Producer")
conf = {
    'bootstrap.servers': 'localhost:19092'
}

print("connecting to Kafka topic...")
producer1 = Producer(conf)
print('connected to kafka')

filename = 'airline_tweets_final.csv'
df = pd.read_csv(filename)

for index, row in df.iterrows():
    dict = {'tweet_id': str(row['tweet_id']),
            'airline_sentiment': str(row['airline_sentiment']),
            'negativereason': str(row['negativereason']) if not row['negativereason'] is None else ' ',
            'airline': str(row['airline']) if not  row['airline'] is None else ' ',
            'name': str(row['name']) if not row['airline'] is None else ' ',
            'retweet_count': str(row['retweet_count']) if not  row['retweet_count'] is None else ' ',
            'text': str(row['text']) if not row['text'] is None else ' ',
            'tweet_coord': str(row['tweet_coord']) if not row['tweet_coord'] is None else ' ',
            'tweet_created': str(row['tweet_created']) if not row['tweet_created'] is None else ' ',
            'tweet_location': str(row['tweet_location']) if not  row['tweet_location'] is None else ' ',
            'user_timezone': str(row['user_timezone']) if not row['user_timezone'] is None else ' '
            }

    tweet_string = json.dumps(dict)

    try:
        producer1.produce(topic=kafka_topic_name, key=str(uuid4()), value=tweet_string.encode('utf-16','surrogatepass'))
        print('published {}'.format(tweet_string))
        producer1.flush()

    except Exception as ex:
        print("Exception happened :", ex)