import markovify
import tweepy, time, sys, random

#Input twitter API info from apps.twitter.com
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Get raw text from corpus as string for markovify
with open("/vagrant/gitstuffs/markovify/test/texts/thermodynamics.txt") as f:
    texta = f.read()
with open("/vagrant/gitstuffs/markovify/test/texts/frankenstein.txt") as f:
    textb = f.read()
	
# Build the model.
text_model_a = markovify.Text(texta)
text_model_b = markovify.Text(textb)

model_combo = markovify.combine([text_model_a,text_model_b],[2,1])

# Print a randomly-generated sentences of no more than 140 characters
status = model_combo.make_short_sentence(140)
api.update_status(status)
#time.sleep(3600) #tweet every 60 minutes