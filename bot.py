"""
Workflow:
-import.py-
1. Obtain CSV of parcels from Leon County's Appraiser's website.
2. Import CSV file as dataframe.
3. Modify dataframe.
-bot.py-
4. Post streetview image of the address (and street name/number) to twitter account.
"""

"""
STEP 4: Posting
"""
#import libraries
import pandas as pd
import tweepy 
import io
import time
import requests
import os

#read csv as dataframe - this file is what was created in import.py
df = pd.read_csv('./lots.csv')[["street", "address", "tweeted"]]

#read YAML file
yaml_file = open("./keys.yaml")
parsed_yaml_file = yaml.load(yaml_file)

#urls for requests to google maps
GCAPI = "https://maps.googleapis.com/maps/api/geocode/json"
SVAPI = "https://maps.googleapis.com/maps/api/streetview?"

#authorization function
def twitter_api():
  auth = tweepy.OAuthHandler(parsed_yaml_file["consumer_key"], parsed_yaml_file["consumer_secret"])
  auth.set_access_token(parsed_yaml_file["access_token"], parsed_yaml_file["access_token_secret"])
  api = tweepy.API(auth)
  return api

#get streetview image function
def post_tweet():
  api = twitter_api()

  for index, row in df.iterrows():
    if (row['street'] != 0) is True: #only posts lots that haven't been tweeted
      #parameters for google street view
      params = {
      "location": row['address'],
      "key": parsed_yaml_file["g_maps_key"],
      "size": "1000x1000",
      "fov": "80", 
      "pitch": "10", 
      }

      #returns static image
      r = requests.get(SVAPI, params=params)

      #saves image at temporary file (sv.png)
      with open('sv.png', 'wb') as image:
        image.write(r.content)

      #creates tweet with file as image and status as lot's street address
      api.update_with_media('sv.png', status=row['street'])
      df.at[row, 'tweeted'] = 1 #updates tweeted number for the lot
      df.to_csv('./lots.csv') #updates lots file
      print(row["street"])
      
      #removes temporary file
      os.remove('sv.png')
      
      #wait ~30 minutes until the next posting
      time.sleep(1780)

#post tweet
post_tweet()
