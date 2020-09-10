import json
import pathlib


def file_reader(filepath):
    "read content of filepath (str) and return content (str)"


def json2dict(json_text):
    "read json_text (str) and return (dictionary)"


def get_config():
    "use file_reader and json2dict to return content of config.json as (dict)"
    this_folder = pathlib.Path(__file__).parent
    text = file_reader(this_folder / "config.json")
    return json2dict(text)

