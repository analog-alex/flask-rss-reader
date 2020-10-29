from flask import json


class Country:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __str__(self):
        return f'Country(code={self.code}, description={self.description})'

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
