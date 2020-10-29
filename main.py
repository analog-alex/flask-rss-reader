from flask import Flask
from src.controllers.IndexController import index_controller
from src.controllers.FeedsController import feeder_controller
from src.repository.elasticsearch import ping


########################################
# entry point for flask app
# - Flask version (1.1.2)
# - by Miguel Alexandre @2020
#
########################################
app = Flask(__name__)

# register controllers
app.register_blueprint(index_controller)
app.register_blueprint(feeder_controller)

# check for ElasticSearch server
pong = ping()
print(f' * Elasticsearch server on -- {pong}')
