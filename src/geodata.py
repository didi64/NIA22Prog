# https://en.wikipedia.org/wiki/Haversine_formula
# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
import math 
def distance(pt1, pt2):
    '''returns distance in meters,
       pt1, pt2: (latitude, longitude)  in degrees
    '''   
    lat1, lng1 = pt1
    lat2, lng2 = pt2
    p = math.pi/180
    a = 0.5 - math.cos((lat2-lat1)*p)/2\
        + math.cos(lat1*p) * math.cos(lat2*p) * (1-math.cos((lng2-lng1)*p))/2
    return 12742000 * math.asin(math.sqrt(a))