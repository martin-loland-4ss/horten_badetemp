import requests
from .readers import get_config


def get_data(api_url):
    "get text from api_url (str) and return content (str)"


def extract_latlon(data):
    "extract latitudes and longitudes from data (list of dict) and return (tuple of two lists with numbers)"


def raw_data_to_dict_list(data):
    """convert data (dict) to (list of dict) 
    where each item in list is feature with 'location', 'coordinate', 'temperature' and 'updated'
    """


def get_features():
    "use get_config and raw_data_to_dict_list functions to return data (list of dict)"
