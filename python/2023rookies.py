import csv

with open('2023rookies.txt', encoding="utf8") as n:
    reader = csv.reader(n, delimiter=",")

    nameList = set()

    for row in reader:
        name = row[0]
        games = row[1]
        brefID = row[2]
        nameList.add(name.split(" ", 1)[-1])
        nameList.add(name.rpartition(' ')[-1])
    print(nameList)
    for name in nameList:
        print("Names.add(\"{0}\")".format(name))