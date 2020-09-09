import requests
from .readers import get_config


def get_data(api_url):
    "get text from api_url (str) and return content (str)"
    r = requests.get(api_url)
    return r.text


def extract_latlon(data):
    "extract latitudes and longitudes from data (list of dict) and return (tuple of two lists with numbers)"
    latitudes = []
    longitudes = []
    for feature in data:
        latitudes.append(feature["location"][0])
        longitudes.append(feature["location"][1])
    return latitudes, longitudes


def raw_data_to_dict_list(data):
    """convert data (dict) to (list of dict) 
    where each item in list is feature with 'location', 'coordinate', 'temperature' and 'updated'
    """
    array = []
    for feature in data["features"]:
        d = {
            "location": feature["geometry"]['coordinates'],
            "temperature": float(feature["properties"]['last']),
            "updated": feature["properties"]['time']
        }
        array.append(d)
    return array


def get_features():
    "use get_config and raw_data_to_dict_list functions to return data (list of dict)"
    config = get_config()