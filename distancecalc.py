import math
# input
# latitude sumbu x, longitude sumbu y
lat1 = -7.9716403
long1 = 112.6317838

lat2 = -7.2574719
long2 = 112.7520883

# process
def distance_on_unit_sphere(lat1, long1, lat2, long2):
    # approximate radius of earth in km
    radius_of_earth_km = 6373.0

    # convert latitude and longitude to spherical coodinates in radians
    degrees_to_radians = math.pi/180.0

    # pi = 90 - latitude
    pi1 = (90.0 - lat1)*degrees_to_radians
    pi2 = (90.0 - lat2)*degrees_to_radians

    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians

    # compute spherical distance from spherical coordinates
    # for two locations in spherical coordinates
    cos = (math.sin(pi1) * math.sin(pi2) * math.cos(theta1 - theta2) + math.cos(pi1) * math.cos(pi2))
    arc = math.acos(cos)

    # remember to multiply arc by the radius of the earth in your favorite et of units to get the length
    distance_km = arc * radius_of_earth_km

    return distance_km

print(distance_on_unit_sphere(lat1, long1, lat2, long2))
# output