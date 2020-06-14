# every lot bot 

This is a fork of the *everylotbot* library by Neil Freeman. It is a Twitter bot that tweets a Google Street View image of every single lot, whether vacant or not, in Tallahassee, FL. It is currently running at [@everylottallahassee](https://twitter.com/everylotinTLH). The purpose of this bot is to bring value to your perception of your city and illuminate disparity -- read more about that [here](http://fakeisthenewreal.org/everylot/).

## what you'll need to build your own
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

You'll need a CSV file of the lots. For @everytreeintlh, I exported a CSV from Leon County's [Property Appraiser site](https://www.leonpa.org/_dnn/).  Here are the fields that were used in the bot:

* For general tracking:
  * id ('PARID')

* For composing the tweets:
  * address ('LOCATION')
  * zip ('ZIP')
  * house number ('HOUSENBR')
  * tax district ('TAXDISTRICT')

* For Google Street View lookups:
  * address

### A place for your bot to live

Now, you just need a place for the bot to live. This needs to be a computer that's always connected to the internet, and that you can set up to run tasks for you. You could use a virtual server hosted at a vendor like Amazon AWS or GCP, or space on a web server.
