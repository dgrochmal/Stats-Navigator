import csv
from pybaseball import playerid_lookup
import pandas as pd
import json

def make_json(csvFilePath, jsonFilePath, jsonKey):
     
    # create a dictionary
    data = {}
     
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            if rows["key_mlbam"]:
                rows["key_mlbam"] = str(int(float(rows["key_mlbam"])))
            if rows["key_fangraphs"]:
                rows["key_fangraphs"] = str(int(float(rows["key_fangraphs"])))
            
            key = rows[jsonKey]
            if key:
                if jsonKey != "key_bbref":
                    key = int(float(key))
            
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        # pretty print
        # jsonf.write(json.dumps(data, indent=4))
        # no whitespace print
        jsonf.write(json.dumps(data, indent=None, separators=(',', ':')))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system
 
# Call the make_json function
# filtered_people.csv filters the chadwick dataset to only players with a savant, fangraphs, and bbref ID
# Rookies from the current year are added via manual mining
make_json(r'filtered_people.csv', r'mlbam.json', 'key_mlbam')
make_json(r'filtered_people.csv', r'fangraphs.json', 'key_fangraphs')
make_json(r'filtered_people.csv', r'bbref.json', 'key_bbref')