from twython import Twython


APP_KEY = 'xxxx'
APP_KEY_SECRET = 'xxxx'
ACCESS_TOKEN = 'xxxx'
TOKEN_SECRET = 'xxxx'

t = Twython(app_key=APP_KEY, app_secret=APP_KEY_SECRET, oauth_token=ACCESS_TOKEN, oauth_token_secret=TOKEN_SECRET)

#auto post status			
t.update_status(status='Testing my twitter bot.')

#scrape tweets and auto respond
tl = t.getUserTimeline()

lastTweet = tl[0]

tid = str(lastTweet['id'])

search = tl.searchTwitter(q = "BasedGod", since_id = tid, rpp = "10")

for tweet in search['results']:
	user = tweet['from_user']
	txt = tweet['text']
	id = str(tweet['id'])
	
	if txt.lower() == "BasedGod" or txt.lower() == "basedgod":
		head = "@" + user + ""
		
		t.update_status(status = head + "TYBG")
