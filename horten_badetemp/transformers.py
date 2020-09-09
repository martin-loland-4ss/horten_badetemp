import arrow


def squared(num):
    return num**2


def average_latlon(latitudes, longitudes):
    "take in latitudes and longitudes (list of numbers) and return averages (tuple of two numbers)"
    return sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes)


def timestamp2human(timestamp):
    "read timestamp (str) and return human x days/hours/minutes ago (str)"
    time = arrow.get(timestamp)
    return time.humanize()
