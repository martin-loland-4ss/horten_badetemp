import json


def file_reader(filepath):
    "read content of filepath (str) and return content (str)"
    with open(filepath, 'r') as f:
        return f.read()


def json2dict(json_text):
    "read json_text (str) and return (dictionary)"