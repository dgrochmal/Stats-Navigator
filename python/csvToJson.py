import csv
import json
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
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
            key = rows['key_mlbam']
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
csvFilePath = r'joined.csv'
jsonFilePath = r'mlbam.json'
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)