# A program to do various things using the Reddit API

# Importing modules
import sys
import json
import urllib2

base_url = "http://www.reddit.com/"

def getUserData(username):
	url = base_url + "user/" + username + ".json"
	
	try:
		data = json.load(urllib2.urlopen(url))
		return data
	except urllib2.HTTPError:
		print("Username does not exist: %s" % username)
		sys.exit(0)
	
	

def getMostRecentPost(username):
	jsonData = getUserData(username)
	return jsonData['data']['children'][0]
	

def getPostStats(username):
	postData = getMostRecentPost(username)
	
	upvotes = postData['data']['ups']
	downvotes = postData['data']['downs']
	stats = {'upvotes': upvotes,'downvotes': downvotes}
	return stats


def main():
	tryAgain = True
	while tryAgain == True:

		user1 = str(raw_input('First user: '))
		user2 = str(raw_input('Second user: '))

		u1Stats = getPostStats(user1)
		u2Stats = getPostStats(user2)
		u1Karma = u1Stats['upvotes'] - u1Stats['downvotes']
		u2Karma = u2Stats['upvotes'] - u2Stats['downvotes']

		if u2Karma > u1Karma:
			print("%s's most recent post (%d|%d) had %d more karma than %s's (%d|%d)" % (user2,u2Stats['upvotes'],u2Stats['downvotes'],(u2Karma - u1Karma),user1,u1Stats['upvotes'],u1Stats['downvotes']))
		elif u1Karma > u2Karma:
			print("%s's most recent post (%d|%d) had %d more karma than %s's (%d|%d)" % (user1,u1Stats['upvotes'],u1Stats['downvotes'],(u1Karma - u2Karma),user2,u2Stats['upvotes'],u2Stats['downvotes']))
		else:
			print("Both posts were equal! (%s: %d|%d vs %s: %d|%d)" % (user1,u1Stats['upvotes'],u1Stats['downvotes'],user2,u2Stats['upvotes'],u2Stats['downvotes']))

		checkTryAgain = raw_input("Try again (y/n)? ")
		checkTryAgain.lower()
		tryAgain = (checkTryAgain == "yes" or checkTryAgain == "y")

if __name__ == '__main__':
	main()


