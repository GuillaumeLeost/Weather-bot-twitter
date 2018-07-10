import os
import urllib2
import json

from twython import Twython
CONSUMER_KEY = 'Yours'
CONSUMER_SECRET = 'yours'
ACCESS_KEY = 'yours'
ACCESS_SECRET = 'yours'

def getweather():
    """ call openweathermap api"""
    response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?lat=yourlat&lon=yourlon&appid=yourapi')
    mydata = response.read()
    return mydata

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

weather = getweather()
w = json.loads(weather)
temp = -273 + int(w['main']['temp']) #--since temp is in kelvin
mylist = ['At', w['name'],',','there is',str(temp),'C']
tweet = " ".join(mylist)

api.update_status(status=tweet)
