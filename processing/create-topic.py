from confluent_kafka.admin import AdminClient, NewTopic

a = AdminClient({'bootstrap.servers': 'localhost:19092'})

new_topics = [NewTopic(topic, num_partitions=1) for topic in ["crypto-ETH-topic"]]

fs = a.create_topics(new_topics)

# fs = a.list_topics()
# print(fs.brokers)
# print(fs.topics)

# fs = a.delete_topics(['crypto-ETH-topic'])
# try:
#     fs = a.create_topics(new_topics)
#     print(fs)
# except Exception as e:
#     print("Failed to create topic {}".format(e))


# # fs = a.delete_topics(new_topics)
# Wait for each operation to finish.
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))
