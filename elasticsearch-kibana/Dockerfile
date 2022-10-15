#
# Elasticsearch Dockerfile
#
# https://github.com/dockerfile/elasticsearch
#

# Pull base image.
FROM ubuntu:20.04

ENV ES_PKG_NAME elasticsearch-8.0.0-linux-x86_64

# Install Java.
RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jre && \
  apt-get install -y wget && \
  rm -rf /var/lib/apt/lists/*

# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Define default command.
CMD ["bash"]

#https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.0.0-linux-x86_64.tar.gz


# Install Elasticsearch.
RUN \
  cd / && \
  wget https://artifacts.elastic.co/downloads/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /elasticsearch-8.0.0 /elasticsearch

# Define mountable directories.
VOLUME ["/data"]

# Mount elasticsearch.yml config
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

RUN useradd elastic --create-home --shell /bin/bash  && \
    chown -R elastic:elastic /home/elastic && \
    chmod 755 /home/elastic && \
    chmod -R 755 /elasticsearch && \
    chmod -R 755 /usr/lib/jvm/java-8-openjdk-amd64 &&




USER elastic

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300