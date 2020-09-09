import requests


def get_data(api_url):
    "get text from api_url (str) and return content (str)"
    r = requests.get(api_url)
    return r.text


def extract_latlon(data):
    "extract latitudes and longitudes from data (dict) and return (tuple of two lists with numbers)"


def raw_data_to_dict_list(data):
    """convert data (dict) to (list of dict) 
    where each item in list is feature with 'location', 'temperature' and 'updated'
    """
    array = []
    for feature in data["features"]:
        d = {
            "location": feature["geometry"]['coordinates'],
            "temperature": feature["properties"]['last'],
            "updated": feature["properties"]['time']
        }
        array.append(d)
    return array
