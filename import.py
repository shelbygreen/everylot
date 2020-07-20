"""
Workflow:
-import.py-
1. Obtain CSV of parcels from Leon County's Appraiser's website.
2. Import CSV file as dataframe.
3. Modify dataframe.
-bot.py-
4. Post streetview image of the address (and street name/number) to twitter account.
"""

#import libraries
import pandas as pd

"""
STEP 2: Importing
"""
#import csv file as dataframe
data = pd.read_csv(r'./Certified_Data.csv')[["PARID","LOCATION","ZIP","HOUSENBR","TAX_DISTRICT"]]

"""
STEP 3: Modifying
"""
#remove lots with insufficient information
df = df.dropna()

#turn zip code, tax district, and housenumber into integers
df['ZIP'] = df['ZIP'].astype(int)
df['TAX_DISTRICT'] = df['TAX_DISTRICT'].astype(int)
df['HOUSENBR'] = df['HOUSENBR'].astype(int)

#remove APT, BLDG, SUITE/STE, OFC, and UNIT from location
df["LOCATION"] = df["LOCATION"].apply(lambda x: x.split(' APT')[0].split(' BLDG')[0].split(' SUITE')[0].split(' STE')[0].split(' OFC')[0].split(' UNIT')[0])

#removes parcels outside of the city and with 0 as the house nmber
df = df.loc[(df['HOUSENBR'] != 0) & (df['TAX_DISTRICT'] != 2)]

#remove any lots with the same street name
df = df.drop_duplicates(subset='LOCATION', keep='first')

#add columns tweeted, city, and state 
df['CITY'] = 'Tallahassee'
df['STATE'] = 'Florida'
df['tweeted'] = 0 

#string concatenation to get parcel's full address
df['FULLADR'] = df['LOCATION'] + ", " + df['CITY'] + ", " + df['STATE'] + ", " + df['ZIP'].astype(str)

#select and rename columns
df = df[["LOCATION","FULLADR","tweeted"]].rename(columns = {'LOCATION':'street', 'FULLADR':'address'})

#shuffle list to randomize order of parcels and reindex dataframe
df = df.sample(frac=1).reset_index(drop=True) 

#save dataframe as csv file 
df.to_csv('./lots.csv')
