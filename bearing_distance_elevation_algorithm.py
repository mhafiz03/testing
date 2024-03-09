import math

def bearing_calculation(pointA, pointB):
    latA = math.radians(pointA[0])
    latB = math.radians(pointB[0])
    lonA = math.radians(pointA[1])
    lonB = math.radians(pointB[1])
    
    delta_lon = lonB - lonA

    x = math.sin(delta_lon) * math.cos(latB)
    y = math.cos(latA) * math.sin(latB) - (math.sin(latA) * math.cos(latB) * math.cos(delta_lon))

    bearing = math.atan2(x, y)
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360
    
    return bearing


def distance_calculation(pointA, pointB):
    # Approximate radius of earth in km
    R = 6373.0

    latA = math.radians(pointA[0])
    latB = math.radians(pointB[0])
    lonA = math.radians(pointA[1])
    lonB = math.radians(pointB[1])
    
    dlon = lonB - lonA
    dlat = latB - latA

    a = math.sin(dlat / 2)**2 + math.cos(latA) * math.cos(latB) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c * 1000
    return distance

def elevation_calculation(pointA, pointB) :
    distance = distance_calculation(pointA, pointB)
    height = 20 #contoh ketinggian pada 20 meter

    pythagoras = math.sqrt(distance**2 + height**2)
    sin_value = height / pythagoras
    arcsin_value = math.asin(sin_value)
    y_axis_angle = math.degrees(arcsin_value)
    
    if y_axis_angle < 60:
        elevation_angle = 60
    elif elevation_angle > 0:
        elevation_angle = 0

    return y_axis_angle

#CONTOH KORDINAT LATITDUR DAN LONGITUDE 2 GPS // UBAH BERDASASARKAN KEBUTUHAN
GPS_1 = (-6.97333, 107.62986)
GPS_2 = (-6.97559, 107.62877)

# https://www.sunearthtools.com/tools/distance.php gunakan web untuk menguji bearing dan distance
# https://www.calculator.net/pythagorean-theorem-calculator.html gunakan web untuk menguji sudut elevasi yang diperlukan untuk y axis

print("Bearing =", bearing_calculation(GPS_1, GPS_2),"°")
print("Distance =", distance_calculation(GPS_1, GPS_2), "m")
print("Y Axis Angle =", elevation_calculation(GPS_1, GPS_2), "°")