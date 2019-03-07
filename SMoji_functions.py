# Import packages
import numpy as np
import pandas as pd
import time 
import requests
import tweepy

from AutTwitter import *
#This file contains the credentials to the Twitter API as well as the PATH to the different files.


def get_weather_number(lat,lon,daystring,timestring,verbose=1):
	#This function connects to the SMHI API gives it geo coordinates and 
	#returns the Weather symbol (int 1-27) of the corresponding day and time
	
	# Assign URL to variable: url
	url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/'+str(lon)+'/lat/'+str(lat)+'/data.json'
	if verbose == 0:
		print(url)

	# Package the request, send the request and catch the response: r
	r = requests.get(url)

	# Decode the JSON data into a dictionary: json_data
	json_data = r.json()

	weather_number = 0
	for time in json_data['timeSeries']:
		if (time["validTime"][8:10] == daystring and time["validTime"][11:16] == timestring):
			for SMHIparameters in time["parameters"]:
				if SMHIparameters["name"] == "Wsymb2":
					 weather_number = SMHIparameters["values"][0]
	
	return weather_number


def weather2emoji(weatherlist):
	#for each one of the Wsymb2 value from SMHI, we associate a given emoji Unicode
	emojifile = PATH+'weatheremojis.xlsx'
	xl = pd.ExcelFile(emojifile) 
	dfemoji = xl.parse(0, index_col=0,usecols=[0,2], names=['SMHI','Unicode']) #we parse the first sheet into an DataFrame using the SMHI code as index
	emojilist = []
	for weatherN in weatherlist:
		emojilist.append(dfemoji.iloc[weatherN-1]['Unicode'])
	return emojilist

def fill_the_map(emojilist):
	#transforms a list of emojis into a text in the shape of Sweden
	emojifile = PATH+'weatheremojis.xlsx'
	xl = pd.ExcelFile(emojifile) 
	dfmap = xl.parse(1,header=None) #we parse the second sheet into an DataFrame
	Tweettext =""
	emoindex = 0
	for index,row in dfmap.iterrows():
		for j in range(8):
			if(row[j] == 0):
				Tweettext += '\u2003'
			else:
				Tweettext += emojilist[emoindex]
				emoindex += 1
		Tweettext +="\n"	
	
	return Tweettext

