# Flask Rss Reader
A micro Flask app (Python) to read RSS feeds into Elasticsearch `@2020`


| Travis CI     | [![Build Status](https://travis-ci.com/analog-alex/flask-rss-reader.svg?branch=main)](https://travis-ci.com/analog-alex/flask-rss-reader) 
| ------------- |:-------------:| 


**Travis CI is no longer in use**

## What is it?

A **Python** (3.7) application built using **Flask** that can read a predefined list of RSS feeds, curated by country, and ingest 
them in a single-node instance of **Elasticsearch**.

## How to run

### Via Docker

Having Docker daemon running simply type in the command line: 
`docker-compose up -d`

### Locally

Must have a instance of Elasticsearch running on port `9200` with not authentication (use `docker-compose up -d elasticsearch` 
from the project root folder)  

Having `Python 3.7` installed with `pip` run:  

1.  `pip install -r requirements.txt`  
2.  `sh run.sh`
