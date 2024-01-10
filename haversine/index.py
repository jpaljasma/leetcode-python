from math import radians, cos, sin, asin, sqrt


def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculates the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """

    # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    _r_miles = 3956
    _r_kilometers = 6371

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    # logitude delta
    dlon = lon2 - lon1
    # latitude delta
    dlat = lat2 - lat1
    # formula
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    # miles or kilometers
    r = _r_miles
    return c * r


# Usage
lon1 = -103.548851
lat1 = 32.0004311
lon2 = -103.6041946
lat2 = 33.374939

print(haversine(lat1, lon1, lat2, lon2))
