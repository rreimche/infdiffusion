## Prerequisites
- python (2.7 was used to develop, I'm not sure if 3 is completely compatible)
- jupyter notebook
- pymongo
- tweepy, twitterscrapper or another system for downloading tweets (see fetcher.py for details)
- argparse
- requests.utils
- re
- mongodb server

## Usage
1. Create a text file with one news headline per line:
> Donald Trump Says Transgender People Should Use the Bathroom They Want
> This may shock you: Hillary Clinton is fundamentally honest | Jill Abramson
> I Miss Barack Obama
> The rise of Donald Trump is a terrifying moment in American politics
> Max Lucado: Trump doesn’t pass the decency test
> No, Not Trump, Not Ever
> John Oliver has the Donald Trump takedown America has been waiting for
> Under Sanders, income and jobs would soar, economist says
> The moment of truth: We must stop Trump

2. `python jobcomposer.py inputfile.txt jobsfile.sh database_name`
3. `chmod +x ./jobsfile.sh && ./jobshile.sh`
4. `python dropextracollections.py database_name`
5. `python tweetseliminator.py database_name`
6. `jupyter notebook`
7. Set database name and (optionally) database server in the beginning of the notebook, go through the whole notebook with Schift+Enter

