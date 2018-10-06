
import praw, json
import time, tweepy
import config

client_id = config.reddit_credentials['client_id']
client_secret = config.reddit_credentials['client_secret']
user_agent = config.reddit_credentials['user_agent']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)



consumer_key = config.twitter_credentials['CONSUMER_KEY']
consumer_secret = config.twitter_credentials['CONSUMER_SECRET']
access_token = config.twitter_credentials['ACCESS_TOKEN']
access_secret = config.twitter_credentials['ACCESS_SECRET']
gmail_user = config.twitter_credentials['gmail_user']
gmail_passwd = config.twitter_credentials['gmail_passwd']


news_titles=[]
news_urls = []

subreddit = reddit.subreddit('ripple')

for submission in subreddit.rising(limit=3):
	news_titles.append(str(submission.title))
	news_urls.append(str(submission.url))

for n in news_titles:
	print(n)

for u in news_urls:
	print(u)

def oauth_authenticate():


	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	print('Returning auth')
	return auth 

def get_tweets(auth):

	api = tweepy.API(auth)

	user = api.get_user('ripple')

	print(user.screen_name)
	print(user.followers_count)

	public_tweets = api.user_timeline('ripple')
	for tweet in public_tweets:
		print(tweet.text)
	


if __name__ == '__main__':

	auth = oauth_authenticate()

	get_tweets(auth)
 




