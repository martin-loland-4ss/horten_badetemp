import ipywidgets
import ipyleaflet
from .data import get_features, extract_latlon
from .transformers import average_latlon, timestamp2human


def get_map(center, zoom):
    "use center (tuple of two numbers) and zoom (number),  return ipyleaflet.Map object"
    return ipyleaflet.Map(
        center=center,
        zoom=zoom,
        scroll_wheel_zoom=True
    )


def popup_html(location, temperature, updated):
    "use location (str), temperature (str) and updated (str), return ipywidgets.HTML object"
    html = f"<b>{location}</b><br>{temperature}&#8451;<br>{updated}"
    return ipywidgets.HTML(html)


def get_marker(coordinate, popup_html):
    "use coordinate (tuple of two numbers) and popup_html (ipywidgets.HTML), return ipyleaflet.Marker object"
    marker = ipyleaflet.Marker(location=coordinate, draggable=False)
    marker.popup = popup_html
    return marker


def get_markers(data):
    """use data (list of dict with keys: 'location', 'coordinate', 'temperature' and 'updated')
    return (list of ipyleaflet.Marker objects), use get_marker, timestamp2human and popup_html function above
    """
    markers = []
    for feature in data:
        html = popup_html(
            location=feature["location"],
            temperature=feature["temperature"],
            updated=timestamp2human(feature["updated"])
        )
        marker = get_marker(coordinate=feature["coordinate"], popup_html=html)
        markers.append(marker)
    return markers


def add_markers_to_map(map, markers):
    """use map (ipyleaflet.Map object) and markers (list of ipyleaflet.Marker objects)
    add markers to map and return (ipyleaflet.Map object)
    """
    for marker in markers:
        map.add_layer(marker)
    return map


def add_fullscreen_control(map):
    "use map (ipyleaflet.Map object), add fullscreen control and return object"
    map.add_control(ipyleaflet.FullScreenControl())
    return map


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
    latitudes, longitudes = extract_latlon(features)
    center = average_latlon(latitudes=latitudes, longitudes=longitudes)
    map = get_map(center=center, zoom=20)
    markers = get_markers(features)
    map = add_markers_to_map(map=map, markers=markers)
    map = add_fullscreen_control(map)
    return map
