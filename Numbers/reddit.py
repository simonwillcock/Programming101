# A program to do various things using the Reddit API

# Importing modules
import json
import urllib2

base_url = "http://www.reddit.com/"

def getUserData(username):
	url = base_url + "user/" + username
	data = json.load(urllib2.urlopen(url))
	return data

print(getUserData(superted125))
