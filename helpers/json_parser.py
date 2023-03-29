import json


class JsonParser:

    @staticmethod
    def read_from_json(json_path):
        with open(json_path, 'r') as json_file:
            json_reader = json.load(json_file)
        return json_reader
