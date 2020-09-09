import requests


def get_data(api_url):
    "get text from website (api_url) and return content (str)"
    r = requests.get(api_url)
    return r.text


def extract_latlon(data):
    "extract latitudes and longitudes from data (dict) and return (tuple of two lists with numbers)"