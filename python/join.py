import pandas as pd
  
# reading csv files
data1 = pd.read_csv('prospectus.csv')
data2 = pd.read_csv('out3-31.csv')
  
data2 = data2.drop(['name_last', 'name_first', 'key_retro', 'mlb_played_first'], axis=1)

outputDF = pd.merge(data1, data2,
                   on=['key_mlbam'],
                   how='right')

outputDF.to_csv('joined.csv', index=False)