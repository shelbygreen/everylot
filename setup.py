"""
Workflow:
-import.py-
1. Obtain CSV of parcels from Leon County's Appraiser's website.
2. Import CSV file as dataframe.
3. Modify dataframe.
-setup.py-
4. Post streetview image of the address (and street name/number) to twitter account.
"""

"""
STEP 4: Posting
"""
#import libraries
import tweepy 
from io import BytesIO
import time
import requests

#read csv as dataframe
df = pd.read_csv(r'./lots.csv')

#urls for requests to google maps
GCAPI = "https://maps.googleapis.com/maps/api/geocode/json"
SVAPI = "https://maps.googleapis.com/maps/api/streetview?"

#authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_streetview_image(g_maps_key, address):
        '''Fetch image from streetview API'''
        params = {
            "location": address,
            "key": g_maps_key,
            "size": "1000x1000",
            "fov": "80", 
            "pitch": "10",
            #other parameters include heading, pitch, and fov 
        }

        r = requests.get(SVAPI, params=params) #goes to streetview

        sv = BytesIO() #takes screenshot of streetview
        for chunk in r.iter_content():
            sv.write(chunk)

        sv.seek(0)
        return sv #returns image file of screenshot

#for loop for making and posting the tweet (photo and street name as the caption)
#posts 1 photo every 1800 seconds, or 30 minutes.
for i, row in df.iterrows():
    image = get_streetview_image(g_maps_key, df['address'][i])
    media = api.media_upload('sv.png', file=image)
    post_result = api.update_status(status=df['street'][i], media_ids=[media.media_id])
    df.at[i, 'tweeted'] = 1
    df.to_csv('./tweeted_lots.csv')
    print(df['address'][i])
    time.sleep(1800) 
