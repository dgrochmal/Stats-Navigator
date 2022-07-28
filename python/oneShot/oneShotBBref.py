import csv
from pybaseball import playerid_lookup
import pandas as pd
import json

with open('prospectus.csv') as n:
    reader = csv.reader(n, delimiter=",")

    # Create a unique list of last names from prospectus data list
    Names = set()
    i = 0
    for row in reader:
        # if (i < 6):
        Names.add(row[0]) 
            # i = i+1      

print(len(Names))
Names.add("Canó")
Names.add("Díaz")
Names.add("Jiménez")
Names.add("Mariñez")
Names.add("Márquez")
Names.add("Mondesí")
Names.add("Rodríguez")
Names.add("Tatís")

list = list(sorted(Names))

lookupLIST = []
df = pd.DataFrame(columns=['name_last', 'name_first', 'key_bbref'])

for name in list:
    df = df.append(playerid_lookup(name))

df['full_name'] = df['name_first'] + ' ' + df['name_last']
df = df.drop(['key_mlbam', 'key_fangraphs', 'key_retro', 'mlb_played_first', "mlb_played_last"], axis=1)

df.to_csv('joinedFullNamebbref.csv', index=False)

def make_json(csvFilePath, jsonFilePath, jsonKey):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # lastPlayed = rows['mlb_played_last']
            # if (lastPlayed is not None and lastPlayed != '' and int(float(rows['mlb_played_last']) > 1915)):
            key = rows[jsonKey].upper()
            data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        # pretty print
        jsonf.write(json.dumps(data, indent=4))
        # no whitespace print
        # jsonf.write(json.dumps(data, indent=None, separators=(',', ':')))
         
# Driver Code
 
# Call the make_json function
make_json(r'joinedFullNamebbref.csv', r'fullnamebbref.json', 'full_name')
# make_json(r'joinedFullName.csv', r'bpid.json', 'bpid')
# make_json(r'joinedFullName.csv', r'fangraphs.json', 'key_fangraphs')
# make_json(r'joinedFullName.csv', r'bbref.json', 'key_bbref')
