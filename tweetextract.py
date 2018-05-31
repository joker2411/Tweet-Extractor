##### MAY-30-2018

import tweepy
import csv
import pandas as pd

####input your credentials here
consumer_key = '***************************'
consumer_secret = '************************'
access_token = '***************************'
access_token_secret = '********************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

####i using the hashtag '#BharatBachao'
# Open/Create a file to append data
csvFile = open('test.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#BharatBachao",count=100,lang="en",since="2018-05-29").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
# tweepy can extract tweets maximum upto 2 weeks back.
