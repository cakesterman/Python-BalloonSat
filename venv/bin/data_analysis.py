import json

# class test_class():
#
#     def __init__(self):
#         self.altitude = 0
#         self.bssid_list = []
#
#
#     def add_bssid(self):
#
#         self.num_bssids += 1
#
#     def set_altitude(self, alt):
#
#         self.altitude = alt
#
# list_of_class = []
# altitude_list = []

data_dict = {}

# added_value = False

# opens and reads a database sorted by altitudes starting from least to greatest
with open('datasamplesSortedAlt.json') as json_file:

    data = json.load(json_file)


    for x in data:

        alt = x['altitude']

        # -------------------------------
        #      Changing Data Structure

        if x['bssid'] == "BSat2019":
            print("SKIPPING")
            continue


        if alt not in data_dict.keys():


            #bssid_list = []

            data_dict[alt] = [x['bssid']]

            print("NOT IN,", data_dict[alt])

        elif alt in data_dict.keys() and x['bssid'] not in data_dict.values():

            if x['bssid'] in data_dict[alt]:

                print("REPEAT")
                continue

            print("IN,", data_dict[alt])

            data_dict[alt].append(x['bssid'])

            print("Adding " , x['bssid'] , "to altitude" , x['altitude'])



        # -------------------------------
        #      Changing Data Structure

        # creates an instance of the class object, TODO: change variable names
        # test_instance = test_class()

        # checks if altitude was already added to the list
        # if x['altitude'] not in altitude_list:
        #
        #     test_instance.set_altitude(x['altitude'])
        #
        #     altitude_list.append(x['altitude'])
        #
        #     added_value = True
        #
        # # critical part, has to be a nested loop to then add all the bssids
        # for add_bssid in data:
        #
        #     # checks the conditions for adding a bssid to the list
        #     if add_bssid['altitude'] == test_instance.altitude \
        #             and add_bssid['bssid'] != "BSat2019" \
        #             and add_bssid['bssid'] \
        #             not in test_instance.bssid_list:
        #
        #         print("Adding BSSID" , add_bssid['bssid'] , " to altitude list " , test_instance.altitude)
        #
        #         test_instance.bssid_list.append(add_bssid['bssid'])
        #
        #         added_value = True
        #
        # if added_value:
        #
        #     list_of_class.append(test_instance)
        #
        #     added_value = False

# variables for tracking the altitude with the highest amount of bssids
highest_num_of_bssid = 0
at_altitude = 0

print(len(data_dict))

for key, value in data_dict.items():

    num_of_bssids = len(value)

    print("At altitude", key, "there are", len(data_dict[key]), "bssid's")


    if num_of_bssids > highest_num_of_bssid:

        highest_num_of_bssid = num_of_bssids
        at_altitude = key

    #print(len(value))



print("Highest number of bssids is" , highest_num_of_bssid , "at altitude" , at_altitude , "m")



#for x in data_dict.values():



# for x, y in data_dict.items():
#
#     print("For altitude" , x, "there are " , y)

# this reads the list of objects in the array TODO: change variable name
# for y in list_of_class:
#
#     if y.altitude != 0:
#
#         if len(y.bssid_list) > highest_num_of_bssid:
#
#             highest_num_of_bssid = len(y.bssid_list)
#             at_altitude = y.altitude


        #print("For altitude " , y.altitude , "m there are " , len(y.bssid_list) , " bssids")




#print(len(list_of_class))

import matplotlib.pyplot as plt

print(data_dict.keys())

fig, ax = plt.subplots()


ax.scatter(list(data_dict.keys()), [len(i) for i in data_dict.values()])
ax.plot(list(data_dict.keys()), [len(i) for i in data_dict.values()])

plt.show()