from flask import Flask
from src.controllers.index_controller import index_controller
from src.controllers.feeds_controller import feeder_controller
from src.repository.elasticsearch import ping

########################################
# entry point for flask app
# - Flask version (1.1.2)
# - by Miguel Alexandre @2020
#
########################################
app = Flask(__name__)


# let's allow request from anywhere
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


# register controllers
app.register_blueprint(index_controller)
app.register_blueprint(feeder_controller)

# check for ElasticSearch server
pong = ping()
print(f' * Elasticsearch server on -- {pong}')
