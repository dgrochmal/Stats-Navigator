import csv

with open('prospectus.csv') as n:
     reader = csv.reader(n, delimiter=",")

     Names = set()
     for row in reader:
        Names.add(row[0])    

print(sorted(Names))