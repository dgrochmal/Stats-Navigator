import csv
import pandas as pd
import json
import unidecode

# Run this in the same directory as the chadwick register data files

# Chadwick data csv columns
# key_person,key_uuid,key_mlbam,key_retro,key_bbref,key_bbref_minors,key_fangraphs,key_npb,key_sr_nfl,key_sr_nba,key_sr_nhl,key_wikidata,name_last,name_first,name_given,name_suffix,name_matrilineal,name_nick,birth_year,birth_month,birth_day,death_year,death_month,death_day,pro_played_first,pro_played_last,mlb_played_first,mlb_played_last,col_played_first,col_played_last,pro_managed_first,pro_managed_last,mlb_managed_first,mlb_managed_last,col_managed_first,col_managed_last,pro_umpired_first,pro_umpired_last,mlb_umpired_first,mlb_umpired_last

def filter_and_write_to_same_file(input_file_path):
    with open(input_file_path, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")

        # Create a list to store filtered rows
        filtered_rows = []

        # Iterate over each row in the CSV file
        for row in reader:
            
            # Check if columns 2, 4, and 6 have values
            if all(row[i] for i in [2, 4, 6]):
                # print(row)
                # decode names
                if row[13]:
                    row[13] = unidecode.unidecode(row[13])
                if row[12]:
                    row[12] = unidecode.unidecode(row[12])
                # only take the columns we want
                filtered_rows.append([row[i] for i in [2, 4, 6, 12, 13]])
        
        return filtered_rows

# rookie file csv columns
# name_first,name_last,key_fangraphs,key_bbref,key_mlbam
def add_rookies(input_file_path):
    with open(input_file_path, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")

        # Create a list to store filtered rows
        filtered_rows = []

        # Iterate over each row in the CSV file
        for row in reader:
            # Check if the row is not empty
            if any(row):
                # Add the row to filtered_rows
                filtered_rows.append(row)
        
        return filtered_rows

hex_chars = [hex(i)[2:] for i in range(0, 16)]

filtered_people = []
# Call the function for each input file
for i in hex_chars:
    filtered_people.extend(filter_and_write_to_same_file(f'../data/people-{i}.csv'))

# append this year's rookies
filtered_people.extend(add_rookies('../data/people-rookies.csv'))
    
# filtered_people.extend(filter_and_write_to_same_file(f'../data/people-test.csv'))

# Write filtered people to new file
with open('filtered_people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_people)


# TODO, the header line is repeated for each file ("key_mlbam,key_bbref,key_fangraphs,name_last,name_first")