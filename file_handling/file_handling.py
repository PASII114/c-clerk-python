
try:
    data = open("data/data.txt", "r")
    # print(data.read()) #loads all the data at once
    print(data.readline()) #reading a single line
    print(data.readlines()) #taking all lines to a list
    # for l in data:
    #     print(l)

    data.close() #closing the data stream
except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(e)

data_write = open("data/data-write.txt", "w")

data_write.write("Pasindu\n")
data_write.write("22\n")
data_write.write("Address - Galle\n")

data_write.close()

data_append = open("data/data-write.txt", "a")

data_append.write("School - All saints' College\n")

data_append.writelines(["test1\n", "test2"])

data_append.close()

with open("data/data-write.txt", "r") as data_file:

    for line in data_file:
        print(line)