# This script goes through a collection of tweets and for every user it removes all her/his tweets except
# the one published first.

import argparse
import pymongo

# parse command line arguments
parser = argparse.ArgumentParser("tweetseliminator")
parser.add_argument("database", help="Database", type=str)
args = parser.parse_args()

# connect to database
client = pymongo.MongoClient()
db = client[args.database]

# get collection names for later use
collections = sorted([col for col in db.collection_names()])


# for testing purposes
#collections = ['test']
#for i in range(10):
#    db['test'].insert_one({
#        "user":"user1",
#        "timestamp": (datetime.datetime.now() + datetime.timedelta(days=i)) # now + i days
#    })

# eliminate successor tweets for every user
for collection in collections:
    initcount =  db[collection].find().count()
    # gather users
    users = set([uname['user'] for uname in db[collection].find({},{"user":1})])

    removedcount = 0

    for user in users:
        # gather tweets
        tweets = list(db[collection].find({"user": user},{"_id":1}).sort("timestamp", pymongo.ASCENDING))
        for tweet in tweets[1:]:
            # delete all tweets of this user that
            db[collection].delete_one({"_id": tweet["_id"]})
            removedcount += 1

    # print "From collection " + collection + " with " + str(initcount) + " tweets removed " + str(removedcount)
