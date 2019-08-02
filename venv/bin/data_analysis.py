import json
import csv
import matplotlib.pyplot as plt
import numpy as np

manufacture_dict = {}
bssid_list = []
bssid_list_stripped = []


def plot_bssid_by_alt(filename):

    data_dict = {}

    # opens and reads a database sorted by altitudes starting from least to greatest
    with open(filename) as json_file:

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

    # Prints the number of BSSIDs at each altitude
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


    print(data_dict.keys())

    fig, ax = plt.subplots()


    #ax.scatter(list(data_dict.keys()), [len(i) for i in data_dict.values()])
    #ax.plot(list(data_dict.keys()), [len(i) for i in data_dict.values()])
    #ax.plot([len(i) for i in data_dict.values()], list(data_dict.keys()))
    ax.scatter([len(i) for i in data_dict.values()], list(data_dict.keys()))

    plt.xlabel("Number of BSSIDs")
    plt.ylabel("Altitude")
    plt.title("Number of BSSIDs at Altitude")

    #plt.bar()

    plt.show()


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


def check_manufactures():

    matched_manu_dict = {}

    parse_manufactures()

    count = 0

    with open('datasamplesBSSID.json') as json_file:

        bssid_dict = json.load(json_file)

        for bssids in bssid_dict:

            temp_bssid = bssids['bssid'].replace(":", "")

            if bssids['bssid'] == "BSat2019" or bssids['bssid'] in bssid_list_stripped or temp_bssid in bssid_list_stripped:

                #print("Duplicate")

                continue

            bssid_list_stripped.append(bssids['bssid'].replace(":", ""))

    print(len(bssid_list_stripped))

    #print(bssid_list)

    for bssids in bssid_list_stripped:

        newString = ""

        for index, letter in enumerate(bssids):

            if index < 6:

                newString += letter
            else:

                break

        if newString in manufacture_dict.keys():

            count += 1

            if manufacture_dict.get(newString) not in matched_manu_dict:

                #print("Creating new key with", manufacture_dict.get(newString))

                matched_manu_dict[manufacture_dict[newString]] = 0

            #elif manufacture_dict.get(newString) in matched_manu_dict:

            matched_manu_dict[manufacture_dict[newString]] += 1

        else:

            print(newString)


            #print("MATCH with", newString, "and", manufacture_dict.get(newString))

    #print(len(matched_manu_dict))

    print(count)

    for x, y in matched_manu_dict.items():

        print(x, y)

    # Output to a CSV file
    with open('Manufacturers According to BSSIDs Logged.csv', 'w') as csv_write_file:

        manu_writer = csv.writer(csv_write_file)

        manu_writer.writerow(["Manufacturer", "Number of matches"])

        for key, value in matched_manu_dict.items():

            manu_writer.writerow([key, value])


    #print(matched_manu_dict)

    plot_manufactures(matched_manu_dict)


def plot_manufactures(dict):

    #plt.barh(list(dict.keys()), dict.values())
    #plt.yscale('log')
    #plt.ylabel("...", labelpad=40)
    plt.figure(figsize=(11,9))
    fig, ax = plt.subplots(figsize=(11,9))
    ax.barh(list(dict.keys()), dict.values())

    plt.xticks(np.arange(0, 121, 10.0))

    plt.ylabel("Manufactures")
    plt.xlabel("Number of BSSID Matches")
    plt.title("Manufacturers According to BSSIDs Logged")

    plt.show()


# Parses 3 different CSV databases and puts the in a dictionary by macID and vendor
def parse_manufactures():

    with open('convertcsv.csv') as csvfile:

        reader = csv.reader(csvfile)

        current_col = 0

        for row in reader:

            if current_col == 0 or current_col == 1:

                manufacture_dict[row[0]] = row[1].strip()

            current_col += 1

            if current_col > 2:

                current_col = 0

    with open('oui.csv') as csvfile2:

        reader = csv.reader(csvfile2)

        current_col = 0

        for row in reader:

            if current_col == 1 or current_col == 2:

                if row[1] not in manufacture_dict.keys():

                    #print("ADDING VALUE")

                    manufacture_dict[row[1]] = row[2]

            current_col += 1

            if current_col > 3:

                current_col = 0
                
    with open('macaddress.io-db.csv') as csvfile3:
        
        reader = csv.reader(csvfile3)
        
        current_col = 0

        for row in reader:

            if current_col == 0 or current_col == 2:

                manufacture_dict[row[0].replace(":", "")] = row[2]

            current_col += 1

            if current_col > 2:

                current_col = 0

    print(len(manufacture_dict))
    #print(manufacture_dict)

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

def analyze_channels():

    channel_dict = {}
    bssid_list2 = []

    with open('datasamplesSortedAlt.json') as json_file:

        data = json.load(json_file)

        for x in data:

            # Iterates to next index if no channel data
            if x['bssid'] in bssid_list2 or x['channel'] == "None" or x['bssid'] == "BSat2019":

                if x['bssid'] in bssid_list2:

                    #print(x['bssid'], "on channel", x['channel'], ", NOT UNIQUE")

                else:
                    #print(x['bssid'], "on channel", x['channel'])

                #print("Skipping")
                continue

            if x['bssid'] not in bssid_list2 and str(x['channel']) not in channel_dict.keys():

                #print(x['channel'])

                channel_dict[str(x['channel'])] = 0
                bssid_list2.append(x['bssid'])

            #print("Adding channel", x['channel'], "with BSSID", x['bssid'])
            channel_dict[str(x['channel'])] += 1
            bssid_list2.append(x['bssid'])

    #plot_channels(channel_dict)

    #print(channel_dict)
    for channel, value in channel_dict.items():

        print("Channel", channel, "had", value, "unique BSSIDs")

    #output_to_csv("Channels with Unique BSSIDs.csv", "Channel", "Number", channel_dict)


def plot_channels(dict):

    plt.figure(figsize=(11,9))
    fix, ax = plt.subplots(figsize=(11,9))

    ax.bar(list(dict.keys()), dict.values())

    plt.yticks(np.arange(0, 121, 10.0))

    plt.xlabel("Channel")
    plt.ylabel("Number of BSSIDs")
    plt.title("Number of BSSIDs on Different Channels")

    #plt.xticks(str(dict.keys().))

    plt.show()




# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


def count_unique_bssids():

    #bssid_list = []
    bssid_list_repeat = []

    with open('datasamplesSortedAlt.json') as json_file1:

        data = json.load(json_file1)

        for x in data:

            if x['bssid'] not in bssid_list and x['bssid'] != "BSat2019":

                bssid_list.append(x['bssid'])

            else:

                bssid_list_repeat.append(x['bssid'])

                #print(x['bssid'], "is a repeat")

    print("There are", len(bssid_list), "unique BSSIDs")
    print("There are", len(bssid_list_repeat), "repeat BSSIDs")


# Currently only set up for 2 col, may change in the future
def output_to_csv(filename, col1_name, col2_name, dict):
    with open(filename, 'w') as csv_write_file:
        writer = csv.writer(csv_write_file)

        writer.writerow([col1_name, col2_name])

        for key, value in dict.items():
            writer.writerow([key, value])


count_unique_bssids()


# plot_bssid_by_alt('datasamplesSortedAlt.json')


# check_manufactures()

analyze_channels()


