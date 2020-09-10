import arrow


def squared(num):
    return num**2


def average_latlon(latitudes, longitudes):
    avg = (latitudes+longitudes)/2
    return avg
    "take in latitudes and longitudes (list of numbers) and return averages (tuple of two numbers)"


def timestamp2human(timestamp):
    "read timestamp (str) and return human x days/hours/minutes ago (str)"
