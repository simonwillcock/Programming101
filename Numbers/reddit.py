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
	# print(json.dumps(getUserData("superted125"),indent=2))
	# print(json.dumps(getMostRecentPost('superted125'),indent=2))
	# print(getPostStats(getMostRecentPost('superted125')))
	print(getPostStats('superted125'))
	print(getPostStats('superted1256'))

if __name__ == '__main__':
	main()


