import numpy as np
import pandas as pd
import time 
# Import packages
import requests
import tweepy
from time import sleep

from AutTwitter import *
from SMoji_functions import *

# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)

auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

# Construct the API instance
api = tweepy.API(auth)  # create an API object


#We load the list of coordinates (lat,lon) where we are going to ask the forecast
coordinates = pd.read_csv(PATH+'grid.csv',header=0)

#let's get the time and fill the day and hour according to what we want from the smhi API
now = time.localtime()
if (now.tm_mday < 10) :
	day = '0'+ str(now.tm_mday)
else :
	day = str(now.tm_mday)
if (now.tm_hour < 10) :
	hour = '0'+ str(now.tm_hour)+':00'
else :
	hour=str(now.tm_hour)+':00'

#for each point of the map we get the weather symbol and store it in a list
weather_list = []
for index,row in coordinates.iterrows():
	lat = row['lat']
	lon = row['lon']
	weather_list.append(get_weather_number(lat,lon,day,hour))

emoji_list = weather2emoji(weather_list)	

#We put the emojimap in the text of the tweet and send it. Note that we need a line of text to start with or the first spaces are ignored.
status = "#Väder från @SMHI kl"+hour[0:2]+":\n"+fill_the_map(emoji_list)
	
#print(status)
#print(len(status))
api.update_status(status)
