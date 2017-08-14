# Fetches twits from Twitter using one of many possible download mechanisms and parameters given via command line arguments
# This particular implementation uses twitterscraper as an example implementation.
# Warning: scraping twitter may be not completely legal in your country.
# You could use tweepy for a legal option that uses Twitter API.

import argparse
import pymongo
from pymongo.errors import BulkWriteError
from twitterscraper import query_tweets


# parse command line arguments
parser = argparse.ArgumentParser("fetcher")
parser.add_argument("database", help="Database to save to", type=str)
parser.add_argument("collection", help="Collection to save to", type=str)
parser.add_argument("query", help="Query", type=str)
parser.add_argument("limit", help="Limit of tweets to download", type=int, default=None)
args = parser.parse_args()

# connect to database
client = pymongo.MongoClient()
db = client[args.database]
collection = db[args.collection]

# get tweets
# other download mechanisms could be used instead of query_tweets() here.
tweets = []
for tweet in query_tweets(args.query, args.limit):
    tweets.append({
        "_id" : tweet.id,
        "timestamp" : tweet.timestamp,
        "user" : tweet.user,
        "fullname" : tweet.fullname,
        "text" : tweet.text
    })

# save tweets to mongodb
try:
    collection.insert_many(tweets)
    print args.collection + " done"

except BulkWriteError as bwe:
    print(bwe.details)
    #you can also take this component and do more analysis
    #werrors = bwe.details['writeErrors']
    raise