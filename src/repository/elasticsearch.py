from elasticsearch import Elasticsearch

es = Elasticsearch()

# ignore 400 cause by IndexAlreadyExistsException when creating an index
es.indices.create(index='feeds', ignore=400)


def ping():
    return es.ping()


def put_in(index, identifier, payload):
    return es.index(index=index, id=identifier, body=payload)
