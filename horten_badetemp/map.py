import ipywidgets
import ipyleaflet


def get_map(center, zoom):
    "use center (tuple of two numbers) and zoom (number),  return ipyleaflet.Map object"


def popup_html(location, temperature, updated):
    "use location (str), temperature (str) and updated (str), return ipywidgets.HTML object"


def get_marker(location, popup_html):
    "use location (tuple of two numbers) and popup_html (str), return ipyleaflet.Marker object"


def get_markers(data):
    """use data (list of dict with keys: 'location', 'temperature' and 'updated')
    return (list of ipyleaflet.Marker objects), use get_marker function above
    """