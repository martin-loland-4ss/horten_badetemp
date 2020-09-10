import requests
from .readers import get_config
from .readers import json2dict


def get_data(api_url):
    "get text from api_url (str) and return content (str)"
    return requests.get(api_url).text


def extract_latlon(data):
    "extract latitudes and longitudes from data (list of dict) and return (tuple of two lists with numbers)"
    
    lat, lon = [], []

    for loc in data:
        lat.append(loc['coordinate'][0])
        lon.append(loc['coordinate'][1])
    
    return lat, lon 

def raw_data_to_dict_list(data):
    """convert data (dict) to (list of dict) 
    where each item in list is feature with 'location', 'coordinate', 'temperature' and 'updated'
    """
    array = []

    for feature in data["features"]:
        loc = feature['properties']['device']
        coordinate = feature['geometry']['coordinates'][::-1]
        temp = float(feature['properties']['last'])
        update = feature['properties']['time']
        
        array.append[{'location':loc, 'coordinate':coordinate,'temperature':temp, 'updated':update}

    return array

def get_features():
    "use get_config, get_data, json2dict and raw_data_to_dict_list functions to return data (list of dict)"
