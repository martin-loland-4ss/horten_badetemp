import ipywidgets
import ipyleaflet
from .data import get_features, extract_latlon
from .transformers import average_latlon, timestamp2human


def get_map(center, zoom):
    "use center (tuple of two numbers) and zoom (number),  return ipyleaflet.Map object"


def popup_html(location, temperature, updated):
    "use location (str), temperature (str) and updated (str), return ipywidgets.HTML object"


def get_marker(coordinate, popup_html):
    "use coordinate (tuple of two numbers) and popup_html (ipywidgets.HTML), return ipyleaflet.Marker object"


def get_markers(data):
    """use data (list of dict with keys: 'location', 'coordinate', 'temperature' and 'updated')
    return (list of ipyleaflet.Marker objects), use get_marker, timestamp2human and popup_html function above
    """


def add_markers_to_map(map, markers):
    """use map (ipyleaflet.Map object) and markers (list of ipyleaflet.Marker objects)
    add markers to map and return (ipyleaflet.Map object)
    """


def add_fullscreen_control(map):
    "use map (ipyleaflet.Map object), add fullscreen control and return object"


def get_master_map():
    """Use the following functions to generate a map:
        get_features
        extract_latlon
        average_latlon
        get_map
        get_markers
        add_markers_to_map
        add_fullscreen_control
        return map (ipyleaflet.Map object)
    """
    features = get_features()
    lat, lon = extract_latlon(features)
    center = avg_latlon(latitudes=lat, longitudes=lon)
    map = get_map(center=center, zoom=11)
    mrk = get_markers(features)
    map = add_markers_to_map(map=map, markers=mrk)
    map = add_fullscreen_control(map)
    return map
