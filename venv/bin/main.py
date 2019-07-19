import json

wifi_database_bssid = []
ballon_bssid = []

def add_bssid(filename) :

    temp_bssid = []

    with open(filename)as json_file:
        data = json.load(json_file)

        for x in data:

            if x['bssid'] in temp_bssid:
                #print("Not unique")
                continue

            else:
                temp_bssid.append(x['bssid'])



    return temp_bssid

def format_bssid(passed_bssid):

    new_bssid_list = []

    for x in passed_bssid:

        current_index = 0
        string_counter = 1

        new_bssid = x

        for individual_character in x:

            #print("Current string count: " + str(string_counter))
            #print("Current character: " + individual_character)
            #print("Current character index: " + str(current_index))

            if string_counter == 3:
                #print(individual_character)
                #print(string_counter)
                new_bssid = new_bssid[:current_index] + ':' + new_bssid[current_index:]
                #print(new_bssid)
                #print("Resestting string counter")
                string_counter = 0

            if current_index == 11:

                new_bssid = new_bssid[:14] + ':' + new_bssid[14:]

            string_counter += 1
            current_index += 1

        new_bssid_list.append(new_bssid)
        #print(new_bssid)

    return new_bssid_list

def compare_bssids(bssid_list1, bssid_list2):

    matches = []

    comparisons = 0

    for x in bssid_list2:

        if x in bssid_list1:
            print("FOUND MATCH")
            matches.append(x)
        else:
            comparisons += 1

    print(comparisons)
    print_bssid_list(matches)

def print_bssid_list(passed_bssid):

    print(len(passed_bssid))

    for bssids in passed_bssid:
        print(bssids)

#Public wifi database
wifi_database_bssid = add_bssid('wifi_zoneMaxBssid.json')
#Data from ballon launched by the army
ballon_bssid = add_bssid('datasamplesBSSID.json')
#Public wifi database
mylnikov = add_bssid('newwifi.json')

#Format the bssid's with colons
wifi_database_bssid = format_bssid(wifi_database_bssid)
mylnikov = format_bssid(mylnikov)
#print_bssid_list(wifi_database_bssid)
#print_bssid_list(ballon_bssid)

compare_bssids(ballon_bssid,wifi_database_bssid)
compare_bssids(ballon_bssid, mylnikov)