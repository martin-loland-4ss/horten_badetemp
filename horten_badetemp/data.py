

def get_data(api_url):
    "get text from website (api_url) and return content (str)"
    return api_url[:2]


def extract_latlon(data):
    "extract latitudes and longitudes from data (dict) and return (tuple of two lists with numbers)"