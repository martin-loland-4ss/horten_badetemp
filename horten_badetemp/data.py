import requests
from .readers import get_config
from .readers import json2dict


def get_data(api_url):
    "get text from api_url (str) and return content (str)"
    r = requests.get(api_url)
    return r.text


def extract_latlon(data):
    "extract latitudes and longitudes from data (list of dict) and return (tuple of two lists with numbers)"
    latitudes = []
    longitudes = []
    for feature in data:
        latitudes.append(feature["coordinate"][0])
        longitudes.append(feature["coordinate"][1])
    return latitudes, longitudes


def raw_data_to_dict_list(data):
    """convert data (dict) to (list of dict) 
    where each item in list is feature with 'location', 'coordinate', 'temperature' and 'updated'
    """
    array = []
    for feature in data["features"]:
        d = {
            "location": feature["properties"]['device'],
            "coordinate": feature["geometry"]['coordinates'][::-1],
            "temperature": float(feature["properties"]['last']),
            "updated": feature["properties"]['time']
        }
        array.append(d)
    return array


def get_features():
    "use get_config, get_data, json2dict and raw_data_to_dict_list functions to return data (list of dict)"
    config = get_config()
    data_text = get_data(api_url=config["api_url"])
    data = json2dict(data_text)
    return raw_data_to_dict_list(data)
