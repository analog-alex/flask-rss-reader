from datetime import datetime

from flask import Response, json, Blueprint

from src.service import countries
from src.service.reader import find_sources_by_country, fetch_all_feeds_by_country, \
    ingest_all_feeds_for_country

feeder_controller = Blueprint('feeder_controller', __name__)


@feeder_controller.route('/feed/countries')
def get_countries():
    return Response(
        response=json.dumps(countries, default=lambda o: o.__dict__, sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )


@feeder_controller.route('/feed/countries/<country_code>')
def get_sources_by_country(country_code):
    return Response(
        response=json.dumps(
            find_sources_by_country(country_code),
            default=lambda o: o.__dict__,
            sort_keys=False,
            indent=4
        ),
        status=200,
        mimetype='application/json'
    )


@feeder_controller.route('/feed/countries/<country_code>/feeds', methods=['GET'])
def get_feeds_by_country(country_code):
    return Response(
        response=json.dumps(
            fetch_all_feeds_by_country(country_code),
            default=lambda o: o.__dict__,
            sort_keys=False,
            indent=4
        ),
        status=200,
        mimetype='application/json'
    )


@feeder_controller.route('/feed/countries/<country_code>/feeds', methods=['PUT'])
def inject_feeds_by_country(country_code):
    response = ingest_all_feeds_for_country(country_code)
    response['at'] = datetime.now().__str__()

    return Response(
        response=json.dumps(response, default=lambda o: o.__dict__, sort_keys=False, indent=4),
        status=200,
        mimetype='application/json'
    )
