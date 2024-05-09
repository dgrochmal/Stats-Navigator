import csv
import pandas as pd
import json
import unidecode

def make_json(csvFilePath, jsonFilePath, jsonKey):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            if rows["key_bbref"]:
                if rows["name_first"]:
                    rows["name_first"] = unidecode.unidecode(rows["name_first"])
                if rows["name_last"]:
                    rows["name_last"] = unidecode.unidecode(rows["name_last"])
                if rows["name_first"] and rows["name_last"]:
                    rows["full_name"] = rows["name_first"] + " " + rows["name_last"]

            if rows["name_first"] and rows["name_last"]:
                key = unidecode.unidecode(rows[jsonKey])
                key = key.upper()
                del rows['key_mlbam']
                del rows['key_fangraphs']
                del rows['name_first']
                del rows['full_name']
                data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        # pretty print
        # jsonf.write(json.dumps(data, indent=4))
        # no whitespace print
        jsonf.write(json.dumps(data, indent=None, separators=(',', ':')))
         
# Driver Code
 
# Call the make_json function
make_json(r'filtered_people.csv', r'fullnamebbref.json', 'full_name')
