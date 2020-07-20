# every lot bot 

This is a fork of the *everylotbot* library by Neil Freeman. It is a Twitter bot that tweets a Google Street View image of every single lot, whether vacant or not, in Tallahassee, FL. It is currently running at [@everylottallahassee](https://twitter.com/everylotinTLH). This bot has no particular purpose. I just hope it brings you some value and illuminates your perception of spatial disparities -- read more about that [here](http://fakeisthenewreal.org/everylot/).

## What You'll Need to Build Your Own

* Python 3.x
* A fresh Twitter account and a Twitter app, with registered keys
* A Google Streetview API token.
* A csv file with a row for every address you're interested in
* A place to run the bot (like a dedicated server or a GCP virtual machine)

### Twitter keys

Creating a Twitter account should be straightforward. To create a Twitter app, register at [apps.twitter.com/](http://apps.twitter.com/). Once you have an app, you'll need to register your account with the app. [Twitter has details](https://dev.twitter.com/oauth/overview/application-owner-access-tokens).

### Streetview key

Visit the [Google Street View Image API](https://developers.google.com/maps/documentation/streetview/) page and get a key.

### Addresses

You'll need a CSV file of the lots. For @everylotintlh, I exported the "Download Certified Tax Roll Data" [CSV](https://www.leonpa.org/_dnn/Downloads/Downloads-Page) from Leon County's [Property Appraiser site](https://www.leonpa.org/_dnn/) and cleaned it up, as shown in the import.py file. 

Here are the fields that were used in the bot:
* tweeted - to track amount of times the lot was tweeted
* address - for google street view lookups
* street - for composing tweets

### A place for your bot to live

You could use a virtual server hosted at a vendor like Amazon AWS or GCP, or space on a web server. I used a GCP Virtual Machine and followed this [tutorial](https://www.youtube.com/watch?v=2d5LzJNj46w) to set it up. 

### Usage
Once you've created lots.csv -- a clean CSV of the lots (with a 'street', 'address' and 'tweeted' column) -- and configured your virtual environment to house your Twitter/Google credentials in the setup.py file, you're ready to go. 

Run: 
'python3 setup.py' in the command line. It will post 1 lot every 30 minutes until it runs out of lots.
