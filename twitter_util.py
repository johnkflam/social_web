import twitter
import json

def get_api():
    CONSUMER_KEY = 'L1wdn5VbX6mvCnD0sFjTWyzNf'
    CONSUMER_SECRET = 'ZiWW5jcNsJ04JIXVmvxqz7QynwZtiMOXd8Ax4ffUbpVnCdWERi'
    OAUTH_TOKEN = '88218932-6nlUJ3Io5OnBtPwnUhjkyMBfhPtuGaB72cvNcnIr9'
    OAUTH_TOKEN_SECRET = 'itTB7MFh480Fl6o3YwmXeDOypH1IbHGaxaWxCYyG4B9FK'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,
                          CONSUMER_KEY,CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def pprint(tweets):
    '''
        pretty print tweets
    '''
    print json.dumps(tweets,indent=1)
