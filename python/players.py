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

list = []
with open('players.csv') as n:
     reader = csv.reader(n, delimiter=",")
     for row in reader:
        x = row[0].replace('\xa0', ' ')
        size = len(x)
        # Slice string to remove last 3 characters from string
        x = x[:size - 11]
        l = x.split()
        lastName = l[1:]
        # print(lastName)     
        list.append(" ".join(lastName))

# list = flatten(list)
list = removeDupes(list)
# print(list)   
print(len(list))

lookupLIST = []
df = pd.DataFrame(columns=['name_last', 'name_first', 'key_mlbam', 'key_bbref', 'key_fangraphs'])

for name in list:
    df = df.append(playerid_lookup(name))
    
df.to_csv('out.csv', index=False)\
