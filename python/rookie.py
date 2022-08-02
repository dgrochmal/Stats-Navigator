import csv

with open('rookies.txt') as n:
    reader = csv.reader(n, delimiter=" ")

    for row in reader:
        first = row[0]
        last = row[1]
        ID = row[2]
        print("if rows[\"key_fangraphs\"] == \"-1\":\n\tif rows[\"name_first\"].upper() == \"{1}\".upper() and rows[\"name_last\"].upper() == \"{0}\".upper():\n\t\trows[\"key_fangraphs\"] = str({2})".format(last, first, ID))