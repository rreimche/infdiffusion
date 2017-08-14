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

>Donald Trump Says Transgender People Should Use the Bathroom They Want  
></Donald>This may shock you: Hillary Clinton is fundamentally honest | Jill Abramson  
>I Miss Barack Obama  

1. `python jobcomposer.py inputfile.txt jobsfile.sh database_name`
The system was developed to copare dynamics of diffusion of real and fake news, so it is important to separate these two types of news. For this you should use 2 input files, 2 output files and 2 databases. It is not necessary to create the databases prior to using this system.
2. `chmod +x ./jobsfile.sh && ./jobshile.sh`
3. `python dropextracollections.py database_name`
4. `python tweetseliminator.py database_name`
5. `jupyter notebook`
6. Go to the web page specified by the command at step 5. You will see 2 notebooks. They are almostly equal, only some labels vary betweetn "fake" and "real". For every (or for one, if you don't want to compare) notebook: set database name and (optionally) database server in the beginning of the notebook, go through the whole notebook with Schift+Enter and enjoy graphs and other results.


