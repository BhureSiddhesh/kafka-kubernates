# kafka spark elasticsearch on Docker Kubernetes
## Airline tweets and cryptocurrency data

[![N|Solid](https://files.readme.io/5c6d2cd-cc-logo.svg)](https://docs.cloud.coinbase.com/exchange/docs/websocket-overview)


### solution Contains following modules
- apache kafka zookeeper for pub/sub architechture
- apache spark for small processing
- elasticsearch for nosql DB and storage with own dockerfile
- kibana for visualization for real time cryptocurrency data
- docker for containing all the deployments 
- kubernetes for orchestration of kafka zookeeper services
- apache nifi for data ingestion


### process (airline tweets)

We have used US Airline tweets data as a source and data will be ingested using a python script , which will read the csv and create json encoded message to ingest to kafa topic 'airline-tweets' running on docker
```sh 
tweet-producer.py
```

Kafka consumer running in python wll read the data from topic 'airline-tweets' and process it in proper format
```
spark-consumer.py
```
Pytohn kafka consumer will connect to spark context running on docker to perform some manipulation on tweets and their raw text
Spark will get the word count fo every tweet and python will create a json request to ingest the entire data to elasticsearch running on docker

We have separate scripts for topic creation and topic deletion for zookeeper running on Docker
```
create-topic.py
```
```
a = AdminClient({'bootstrap.servers': 'localhost:19092'})
new_topics = [NewTopic(topic, num_partitions=1) for topic in ["airline-tweet-topic"]]
fs = a.create_topics(new_topics)

for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))
```

### process (cryptocurrency data from COINBASE)
Python script crypto-producer.py will hit web socket api and fech the live stream data for Etherium currency current value and trading volume
```
crypt-producer.py
```
```
wss://ws-feed.exchange.coinbase.com
```
Header value required to be paased to the above socket address is as follow
```
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
```


Consumer file will read the message string decode it and make to suitable for ingestion and ingest into elasticsearch with different index
```
crypto-consumer.py
```


> The overriding design goal for Markdown's
> formatting syntax is to make it as readable


This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Docker

I have Created separete images for kafka/zookeeper apache and elasticsearch/kibana
I kept default configuation for elasticsearch docker and kibana docker ports 



By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```




Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```


## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
