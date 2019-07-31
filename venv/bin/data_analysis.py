import json

data_dict = {}


# opens and reads a database sorted by altitudes starting from least to greatest
with open('datasamplesSortedAlt.json') as json_file:

    data = json.load(json_file)


    for x in data:

        # -------------------------------
        #      Changing Data Structure

        alt = x['altitude']

        # Checks to see if bssid is BSat2019 and if so, skip this iteration (it's junk data)
        if x['bssid'] == "BSat2019":
            continue

        # if altitude is not a key, adds it as a key
        if alt not in data_dict.keys():

            data_dict[alt] = [x['bssid']]

        elif alt in data_dict.keys() and x['bssid'] not in data_dict.values():

            # This if checks to see if the bssid is already in the key value list, we don't want duplicates
            if x['bssid'] in data_dict[alt]:

                continue

            data_dict[alt].append(x['bssid'])

            print("Adding " , x['bssid'] , "to altitude" , x['altitude'])

        # -------------------------------
        #      Changing Data Structure

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

#print(len(list_of_class))


# Below is working to display the data in charts
import matplotlib.pyplot as plt

print(data_dict.keys())

fig, ax = plt.subplots()


ax.scatter(list(data_dict.keys()), [len(i) for i in data_dict.values()])
ax.plot(list(data_dict.keys()), [len(i) for i in data_dict.values()])

plt.show()