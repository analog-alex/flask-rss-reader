# Flask Rss Reader
A micro Flask app (Python) to read RSS feeds into Elasticsearch

## What is it?

A **Python** (3.7) application built using **Flask** that can read a predefined list of RSS feeds, curated by country, and ingest 
them in a single-node instance of **Elasticsearch**.

## How to run ?

### Via Docker

Having Docker daemon running simply type in the command line: 
`docker-compose up -d`

### Locally

Having `Python 3.7` installed with `pip` run:  

1 -  `pip install -r requirements.txt`  
2 -  `sh run.sh`

