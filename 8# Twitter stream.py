from tweepy import Stream, API
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

#consumer key, consumer secret, access token, access secret.
'''
import credentials
ckey = credentials.ckey
csecret = credentials.csecret
atoken = credentials.atoken
asecret = credentials.asecret
'''

# The keys below are fake and won't work. Replace with your own API keys
ckey="gXgufW08fGkwp60RxhVMhxRGR"
csecret="18d5rhEq6zOY8RsDXyvFX491MaZamUoYsJrRz15azhOBOQsHnC"
atoken="29711oI2dJtDl137582-DktEPqqkuNiVb88kmRD12wHbA70Rgh"
asecret="hyEs0bodUoH3yZQM6jyl8hQEezuv4GF6nXRBjD8iZ2jL7"

class listener(StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        print('************')
        print(decoded['user']['screen_name'])
        print(decoded['text'].encode('ascii', 'ignore'))
        return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
#%% Search API
api = API(auth)
tweets = api.search('Lenddo')
for tweet in tweets[:10]:
    if tweet.lang == 'en':
        print('**********************************************************')
        print(tweet.text)

# Regex to remove @...  ==> re.findall('@\w+',tweet.text)
# Regex to remove links ==> re.findall('http.+',tweet.text)

#%% Stream API
now = time.time()
stoptime = now + 10
print('======== Start streaming ========')
while time.time()<stoptime:
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["marvel"])
print('======== Stop streaming ========')