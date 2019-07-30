import json

class test_class():

    def __init__(self):
        self.altitude = 0
        self.bssid_list = []


    def add_bssid(self):

        self.num_bssids += 1

    def set_altitude(self, alt):

        self.altitude = alt

list_of_class = []
altitude_list = []

with open('datasamplesSortedAlt.json') as json_file:

    data = json.load(json_file)

    for x in data:

        test_instance = test_class()

        if x['altitude'] not in altitude_list:

            test_instance.set_altitude(x['altitude'])

            altitude_list.append(x['altitude'])


        for add_bssid in data:

            if add_bssid['altitude'] == test_instance.altitude \
                    and add_bssid['bssid'] != "BSat2019" \
                    and add_bssid['bssid'] \
                    not in test_instance.bssid_list:

                print("Adding BSSID" , add_bssid['bssid'] , " to altitude list " , test_instance.altitude)

                test_instance.bssid_list.append(add_bssid['bssid'])

        list_of_class.append(test_instance)

highest_num_of_bssid = 0
at_altitude = 0

for y in list_of_class:

    if y.altitude != 0:

        if len(y.bssid_list) > highest_num_of_bssid:

            highest_num_of_bssid = len(y.bssid_list)
            at_altitude = y.altitude


        print("For altitude " , y.altitude , "m there are " , len(y.bssid_list) , " bssids")

print("Highest number of bssids is" , highest_num_of_bssid , "at altitude" , at_altitude , "m")


print(len(list_of_class))