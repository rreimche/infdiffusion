# Creates jobs to fetch tweets from twitter for the timeframe since 2016-01-01 until 2016-12-31

import argparse
from requests.utils import quote

# parse command line arguments
parser = argparse.ArgumentParser("jobcomposer")
parser.add_argument("inputfile", help="Filename to parse for headlines", type=str)
parser.add_argument("outputfile", help="Filename to parse for headlines", type=str)
parser.add_argument("database", help="Database to save to", type=str)
parser.add_argument("--limit", help="Max number of tweets to scrap", type=int, default=10000, required=False)
args = parser.parse_args()

# open files
headlines = open(args.inputfile,"r")
jobs = open(args.outputfile,"w")

# construct shell commands that use fetcher and write them to file
count = 0
for line in headlines.read().split("\n"):
    for i in range(3):
        encoded_query = quote(line) + "%20since%3A2016-01-01%20until%3A2016-12-31"
        job = "python fetcher.py " + args.database + " _" + str(count) + "_" + str(i) + " " + encoded_query + " " + str(args.limit) + "\n"
        jobs.write(job)
    count += 1

# close files
headlines.close()
jobs.close()
