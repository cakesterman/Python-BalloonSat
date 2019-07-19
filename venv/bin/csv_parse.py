import csv

with open('wifi.csv') as csvfile:

    first_line = True

    with open('newwifi.csv', 'w') as csv_write_file:

        wifi_reader = csv.reader(csvfile)
        wifi_writer = csv.writer(csv_write_file)
        for row in wifi_reader:

            if first_line:
                first_line = False
                continue

            lat = float(row[2])
            long = float(row[3])

            if long > -77.5672 and long < -73.3269:

                if lat > 41.146 and lat < 42.2454:

                    #bssid = row[1]
                    print(", ".join(row))

                    wifi_writer.writerow([row[1], lat, long])




