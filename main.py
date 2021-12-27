import csv

data = open("data.txt")
data_list = []

# get the response times from the data
for line in data.readlines():
    stripped_line = line.strip()
    if len(line) <= 45:
        data_list.append(1000)
    else:
        print(line[34])
        first_int = line[34]
        second_int = line[35]
        data_list.append(first_int + second_int)

# write the data to the csv file
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    time_interval = 0
    for entry in data_list:
        writer.writerow([time_interval, entry])
        time_interval += 1


print(data_list)
