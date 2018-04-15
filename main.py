from flask import Flask
from flask import redirect, url_for, request, render_template
from StringMatcher import KMP
from TweetGetter import TweetGetter
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
	return "test"

if __name__ == '__main__':
	# app.debug = True
	# app.run()
	
	api = TweetGetter('credentials.json')
	tweets = api.search_tweets("selamat")

	pprint(tweets)