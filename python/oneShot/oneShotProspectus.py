import csv
from pybaseball import playerid_lookup
import pandas as pd
import json

# # reading csv files
df = pd.read_csv('prospectus.csv')

df['full_name'] = df['name_first'] + ' ' + df['name_last']

df = df.drop(['key_mlbam'], axis=1)

df.to_csv('joinedFullNameProspectus.csv', index=False)

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
make_json(r'joinedFullNameProspectus.csv', r'fullnameProspectus.json', 'full_name')
# make_json(r'joinedFullName.csv', r'bpid.json', 'bpid')
# make_json(r'joinedFullName.csv', r'fangraphs.json', 'key_fangraphs')
# make_json(r'joinedFullName.csv', r'bbref.json', 'key_bbref')
