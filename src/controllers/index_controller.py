from datetime import datetime

from flask import Blueprint

index_controller = Blueprint('index_controller', __name__)


@index_controller.route('/')
def index():
    return f'Server up at {datetime.now()}'
