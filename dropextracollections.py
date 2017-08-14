# For a given database for this script removes 2 of 3 collections with names lie "colnameN", where N if from 0 to 2. O
# Only the collection with maximum tweets is left.

import argparse
import pymongo
import re

from bson import SON

# parse command line arguments
parser = argparse.ArgumentParser("dropextracollections")
parser.add_argument("database", help="Database", type=str)
args = parser.parse_args()

# connect to database
client = pymongo.MongoClient()
db = client[args.database]

# get collection names
collections = sorted([col for col in db.collection_names()])

# drop extra collections
for collection in collections:

    # a dictionary of collections to remove, the key is collection name, the value is the count of tweets in it
    to_remove = dict()

    # get headline id
    headline_id = re.search('(\d+)', collection).group(0)

    # get number of tweets for every of 3 collections related to the same headline
    for i in range(3):
        to_remove[headline_id + "_" + str(i)] = db[headline_id + "_" + str(i)].count()

    # find out, which collection has maximum tweets
    the_one = (headline_id + "_" + str(0), to_remove[headline_id + "_" + str(0)])
    for i in [1,2]:
        if to_remove[headline_id + "_" + str(i)] >= the_one[1]:
            the_one = (headline_id + "_" + str(i), to_remove[headline_id + "_" + str(i)])

    # remove the collection with maximum number of tweets from this dictionary,
    # because it is a list of collections to drop
    del to_remove[the_one[0]]

    # drop collections and remove their names from "collections"
    for col in to_remove.keys():
        db[col].drop()
        if col in collections:
            collections.remove(col)