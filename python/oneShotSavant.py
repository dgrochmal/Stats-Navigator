import csv
from pybaseball import playerid_lookup
import pandas as pd
import json
import unidecode

with open('prospectus.csv') as n:
    reader = csv.reader(n, delimiter=",")

    # Create a unique list of last names from prospectus data list
    Names = set()
    i = 0
    for row in reader:
        Names.add(row[0])  

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
df = pd.DataFrame(columns=['name_last', 'name_first', 'key_mlbam'])

for name in list:
    df = df.append(playerid_lookup(name))

df['full_name'] = df['name_first'] + ' ' + df['name_last']
df = df.drop(['key_bbref', 'key_fangraphs', 'key_retro', 'mlb_played_first', "mlb_played_last"], axis=1)

df.to_csv('joinedFullNameSavant.csv', index=False)

def make_json(csvFilePath, jsonFilePath, jsonKey):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            if rows["key_mlbam"]:
                if rows["name_first"]:
                    rows["name_first"] = unidecode.unidecode(rows["name_first"])
                if rows["name_last"]:
                    rows["name_last"] = unidecode.unidecode(rows["name_last"])
                if rows["full_name"]:
                    rows["full_name"] = unidecode.unidecode(rows["full_name"])

            key = unidecode.unidecode(rows[jsonKey])
            key = key.upper()
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
make_json(r'joinedFullNameSavant.csv', r'fullnamesavant.json', 'full_name')
