## Prerequisites
- python (2.7 was used to develop, I'm not sure if 3 us completely compatible)
- jupyter notebook
- pymongo
- tweepy, twitterscrapper or another system for downloading tweets (see fetcher.py for details)
- argparse
- requests.utils
- re
- mongodb server

## Usage
1. Create a text file with one news headline per line
2. `python jobcomposer.py inputfile.txt jobsfile.sh database_name`
3. `chmod +x ./jobsfile.sh && ./jobshile.sh`
4. `python dropextracollections.py database_name`
5. `python tweetseliminator.py database_name`
6. `jupyter notebook`
7. Set database name and (optionally) database server, go through the whole notebook with Schift+Enter

