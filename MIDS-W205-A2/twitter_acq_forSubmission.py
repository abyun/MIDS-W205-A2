#W205.3 - Al Byun
#Assignment 2
#1. Write an acquisition program to pull the tweets for each hashtag and the tweets that have both of the hashtags simultaneously with in a week. You also need to chunk your data (using your design decisions) and give yourself the ability to re-run the process reliable in case of failures (Resiliency).
#2. Organize the resulting raw data into a set of tweets and store these tweets into S3.

import sys
import tweepy
import datetime
import urllib
import signal
import json
import os

# Change default encoding to prevent any UnicodeEncodeErrors
reload(sys)
sys.setdefaultencoding("utf-8")

# Part 1: Search through Twitter for user inputted search term
#       In command prompt, user will have to type:
#       python twitter_acq.py "#Warriors"
#       python twitter_acq.py "#NBAFinals2015"
#       python twitter_acq.py "#Warriors #NBAFinals2015"

# pip install tweepy
consumer_key = "";
consumer_secret = "";
access_token = "";
access_token_secret = "";
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
q = urllib.quote_plus(sys.argv[1])  # URL encoded query 

# tweet acquisition code
def interrupt(signum, frame):
   print "Interrupted, closing ..."
   exit(1)

class TweetSerializer:
   out = None
   first = True
   count = 0
   def start(self):
      self.count += 1
      fname = 'tweets-'+str(self.count)+'.json'
      self.out = open(fname,'w')
      self.out.write("[\n")
      self.first = True

   def end(self):
      if self.out is not None:
         self.out.write("\n]\n")
         self.out.close()
         
         # Create text files with the tweets parsed out
         file_directory = 'tweets-'+str(self.count)+'.json'
         json_data=open(file_directory).read()
         data = json.loads(json_data)
         
         fname2 = 'tweets-parsed-'+str(self.count)+'.txt'
         out2 = open(fname2,'w')
         for item in data:                  
             out2.write(item.get(u'text'))
             out2.write("\n") 
               
      self.out = None

   def write(self,tweet):
      if not self.first:
         self.out.write(",\n")
      self.first = False
      self.out.write(json.dumps(tweet._json).encode('utf8'))

serializer = TweetSerializer()
serializer.start()
i=0
	
for tweet in tweepy.Cursor(api.search,q=q,since='2015-06-07',until='2015-06-14').items():
    # FYI: JSON is in tweet._json
    i+=1
    if i%100 == 0:
        serializer.write(tweet)
        signal.signal(signal.SIGINT, interrupt)
        serializer.end()
        serializer.start()
    else:
        serializer.write(tweet)
        signal.signal(signal.SIGINT, interrupt)
	
serializer.end()


# Part 2: Find all text/json files in directory (these are the files with the tweets)
#       Upload those files to the S3 bucket
from boto.s3.connection import S3Connection
conn = S3Connection('', '')   ################ REMEMBER TO DELETE THIS PRIOR TO UPLOADING TO GITHUB
bucket = conn.create_bucket('june7_14_warriors_nbafinals2015_tweets')

# Push the tweet text/json files to S3 bucket 
from boto.s3.key import Key

for file in os.listdir("C:\\Users\\Albert\\desktop\\github\\Assignment2\\"):
    if file.endswith(".json"):
        myKey = Key(bucket)
        myKey.key = file
        myKey.set_contents_from_filename(file)