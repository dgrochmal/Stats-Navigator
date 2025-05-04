import csv
import pandas as pd
import json
import unidecode

# Chadwick data csv columns
# key_person,key_uuid,key_mlbam,key_retro,key_bbref,key_bbref_minors,key_fangraphs,key_npb,key_sr_nfl,key_sr_nba,key_sr_nhl,key_wikidata,name_last,name_first,name_given,name_suffix,name_matrilineal,name_nick,birth_year,birth_month,birth_day,death_year,death_month,death_day,pro_played_first,pro_played_last,mlb_played_first,mlb_played_last,col_played_first,col_played_last,pro_managed_first,pro_managed_last,mlb_managed_first,mlb_managed_last,col_managed_first,col_managed_last,pro_umpired_first,pro_umpired_last,mlb_umpired_first,mlb_umpired_last

# Remove the columns we don't care about
def filter_and_write_to_same_file(input_file_path):
    df = pd.read_csv(input_file_path, dtype=str)
    # Drop the specified columns if they exist
    columns_to_remove = ["key_person", "key_uuid", "key_retro", "key_bbref_minors", "key_npb", "key_sr_nfl", "key_sr_nba", "key_sr_nhl", "key_wikidata", "name_given", "name_suffix", "name_matrilineal", "name_nick", "birth_year", "birth_month", "birth_day", "death_year", "death_month", "death_day", "pro_played_first", "pro_played_last", "col_played_first", "col_played_last", "pro_managed_first", "pro_managed_last", "mlb_managed_first", "mlb_managed_last", "col_managed_first", "col_managed_last", "pro_umpired_first", "pro_umpired_last", "mlb_umpired_first", "mlb_umpired_last"]
    df.drop(columns=[col for col in columns_to_remove if col in df.columns], inplace=True)
    df.to_csv(input_file_path, index=False)

# Filter out rows that don't have savant or bbref
def filter_dataless(input_file_path, fileNum):
    with open(input_file_path, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")

        # Create a list to store filtered rows
        filtered_rows = []

        if fileNum != '0':
            next(reader, None)  # Skip the header row

        # Iterate over each row in the CSV file
        for row in reader:
            
            # Check if columns 2, 4, and 6 have values
            if all(row[i] for i in [0, 1]):
                # print(row)
                # decode names
                if row[4]:
                    row[4] = unidecode.unidecode(row[4])
                if row[3]:
                    row[3] = unidecode.unidecode(row[3])
                # only take the columns we want
                filtered_rows.append(row)
        
        return filtered_rows


hex_chars = [hex(i)[2:] for i in range(0, 16)]

for i in hex_chars:
    filter_and_write_to_same_file(f'./people-{i}.csv')

filtered_people = []
for i in hex_chars:
    filtered_people.extend(filter_dataless(f'./people-{i}.csv', i))

with open('filtered_people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_people)
