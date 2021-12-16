import csv
from pybaseball import playerid_lookup
import pandas as pd

def flatten(t):
    return [item for sublist in t for item in sublist]

def removeDupes(test_list):
    res = []
    for i in test_list:
        if i not in res:
            res.append(i)
    return res

with open('prospectus.csv') as n:
     reader = csv.reader(n, delimiter=",")

     Names = set()
     for row in reader:
        Names.add(row[0])    

print(len(Names))

list = list(sorted(Names))

lookupLIST = []
df = pd.DataFrame(columns=['name_last', 'name_first', 'key_mlbam', 'key_bbref', 'key_fangraphs'])

for name in list:
    df = df.append(playerid_lookup(name))
    
df.to_csv('out3.csv', index=False)
