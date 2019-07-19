import piexif
import json
from PIL import Image
from exif_rotate import rotate_jpeg

def format_pictures():

    with open('datasamplesLatLongAlt.json') as json_file:

        data = json.load(json_file)

        photoList = []

        latitude = 0
        longitude = 0
        altitude = 0
        pictue_name = ""

        for x in data:

            if x['pic_filename'] in photoList:
                #print("Not unique")
                continue

            else:
                photoList.append(x['pic_filename'])

                latitude = x['latitude']
                longitude = x['longitude']
                altitude = x['altitude']
                pictue_name = "piCam Photos/" + x['pic_filename']
                #pictue_name = x['pic_filename']

                add_gps_exif(pictue_name, latitude, longitude, altitude)
                rotate_jpeg(pictue_name)




def add_gps_exif(filename, latitude, longitude, altitude):

    path = filename

    img = Image.open(path)

    exif_dict = piexif.load(img.info['exif'])

    #print(exif_dict)

    # Checks the latitude is between certain bounds for North and South
    if latitude >= 0:
        exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = "N"
    elif latitude < 0:
        exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = "S"

    #Checks the longitude is between certain bounds for East and West
    if longitude >= 0:
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = "E"
    elif longitude < 0:
        exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = "W"

    # Setting Altitude, latitude, and longitude
    #NOTE, digits can only be up to a certain length long, maybe 7 or 9

    altitude_converted = convert_to_fraction(altitude)
    latitude_converted = convert_to_fraction(latitude)
    longitude_converted = convert_to_fraction(longitude)

    #print(altitude_converted[0])
    #print(latitude_converted[0])
    #print(longitude_converted[0])

    exif_dict['GPS'][piexif.GPSIFD.GPSAltitude] = (int(altitude_converted[0]), int(altitude_converted[1]))

    exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = (int(latitude_converted[0]), int(latitude_converted[1]))

    exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = (int(longitude_converted[0]), int(longitude_converted[1]))

    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, path)

    print("FINISHED " + filename)



def convert_to_fraction(lat_or_long):

    #Convert to string and cut off any necessary digits

    #print(len(str(lat_or_long)))

    temp_value = str(lat_or_long)
    new_str = ""

    denominator_digits = 0

    #Checks if the length is greater than 9 digits, if it is it strips all digits after 9
    if len(temp_value) > 9:

        string_counter = 0

        for x in temp_value:

            #print(string_counter)

            if x == "-":
                continue

            #10 because decimal is counted as a position
            elif string_counter >= 10:
                break

            new_str = new_str + x

            string_counter += 1

        #print(new_str)
        #print(len(new_str))

        test_return = count_decimal_places(new_str)

        denominator_digits = int(test_return[0])
        temp_value = test_return[1]

        #print(test_return)

        #temp_value = new_str
        #print(temp_value)

    else:

        for x in temp_value:

            #print("HERE")

            if x == "-":
                continue

            new_str = new_str + x

        test_return = count_decimal_places(new_str)
        #print(test_return)

        denominator_digits = int(test_return[0])
        temp_value = test_return[1]

        #temp_value = new_str

    temp_denom = "1"

    for x in range(denominator_digits):

        temp_denom = temp_denom + "0"

    numerator = temp_value
    denominator = temp_denom

    #print(numerator)
    #print(denominator)

    return numerator, denominator

def count_decimal_places(decimal_number):

    #Do something

    temp_string = str(decimal_number)

    decimal_counter = 0

    new_str = ""

    seen_decimal = False

    for x in temp_string:

        if x == '.':

            seen_decimal = True
            continue

        if seen_decimal:

            decimal_counter += 1

        new_str = new_str + x

    #print (new_str)

    return str(decimal_counter), new_str

format_pictures()

#exif_dict = {"GPS" : gps_info}
#exif_bytes = piexif.dump(exif_dict)

#im = Image.open(path)
#piexif.insert(path, exif_bytes)

#exif_dict = piexif.load(path)
#print(exif_dict)