from flask import json


class Feed:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return f'Feed(name={self.name}, url={self.url})'

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
