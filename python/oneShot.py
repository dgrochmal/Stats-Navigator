import csv
from pybaseball import playerid_lookup
import pandas as pd
import json
from fangraphsFixer import *

with open('prospectus.csv') as n:
    reader = csv.reader(n, delimiter=",")

    # Create a unique list of last names from prospectus data list
    Names = set()
    for row in reader:
        Names.add(row[0])    
# Names.add("Downs")
print(len(Names))
Names.add("Canó")
Names.add("Díaz")
Names.add("Jiménez")
Names.add("Mariñez")
Names.add("Márquez")
Names.add("Mondesí")
Names.add("Rodríguez")
Names.add("Tatís")

print(len(Names))

list = list(sorted(Names))

lookupLIST = []
df = pd.DataFrame(columns=['name_last', 'name_first', 'key_mlbam', 'key_bbref', 'key_fangraphs'])

for name in list:
    df = df.append(playerid_lookup(name))
    
# df.to_csv('out3-31.csv', index=False)

# reading csv files
data1 = pd.read_csv('prospectus.csv')
data2 = df
  
data2 = data2.drop(['name_last', 'name_first', 'key_retro', 'mlb_played_first', 'mlb_played_last'], axis=1)

outputDF = pd.merge(data1, data2,
                   on=['key_mlbam'],
                   how='right')

outputDF.to_csv('joined.csv', index=False)

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
            
            if rows["bpid"]:
                rows["bpid"] = str(int(float(rows["bpid"])))
                # if rows["mlb_played_last"]:
                #     rows["mlb_played_last"] = str(int(float(rows["mlb_played_last"])))
            if rows["key_mlbam"]:
                rows["key_mlbam"] = str(int(float(rows["key_mlbam"])))
            if rows["key_bbref"] == "":
                if rows["name_first"] == "JJ" and rows["name_last"] == "Bleday":
                    rows["key_bbref"] = "bledajj01"

            rows = fixFangraphs(rows)
 
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
make_json(r'joined.csv', r'mlbam.json', 'key_mlbam')
make_json(r'joined.csv', r'bpid.json', 'bpid')
make_json(r'joined.csv', r'fangraphs.json', 'key_fangraphs')
make_json(r'joined.csv', r'bbref.json', 'key_bbref')
