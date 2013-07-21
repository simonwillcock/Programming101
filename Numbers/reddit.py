# A program to do various things using the Reddit API

# Importing modules
import json
import urllib2

base_url = "http://www.reddit.com/"

def getUserData(username):
	url = base_url + "user/" + username + ".json"
	
	try:
		data = json.load(urllib2.urlopen(url))
	except urllib2.HTTPError:
		return {"error": "Username does not exist"}
	return data

def getMostRecentPost(username):
	jsonData = getUserData(username)
	if 'error' in jsonData:
		return jsonData
	else:
		post = jsonData['data']['children'][0]
		return post
	

def getPostStats(username):
	postData = getMostRecentPost(username)
	if 'error' in postData:
		return postData
	else:
		upvotes = postData['data']['ups']
		downvotes = postData['data']['downs']
		stats = {'upvotes': upvotes,'downvotes': downvotes}
		return stats

def main():
	user1 = 'superted125'
	user2 = 'Kale21'
	u1Stats = getPostStats(user1)
	u2Stats = getPostStats(user2)
	u1Karma = u1Stats['upvotes'] - u1Stats['downvotes']
	u2Karma = u2Stats['upvotes'] - u2Stats['downvotes']
	if u2Karma > u1Karma:
		print("%s's most recent post had %d more karma than %s's" % (user2,(u2Karma - u1Karma),user1))
	elif u1Karma > u2Karma:
		print("%s's most recent post had %d more karma than %s's" % (user1,(u1Karma - u2Karma),user2))
	else:
		print("Both posts were equal!")


if __name__ == '__main__':
	main()


