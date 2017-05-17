# jobnotif
Quick and dirty python script that uses beautifulsoup to scrape a url and send an email through smtp if a job matching a substring is found.
~~Wanted to keep track of Twitch's internship opportunities but no option to automatically email is available.
Keeps track of duplicate jobs with a set stored using pickle.~~
Made this slightly more generic, to add a new parser write a concrete implementation of the BaseParser class, and put a clause in the parser_factory class to construct it. Still only has Twitch available, but in theory actually works for any lever.co type of job page.

Output email is in the form of:
~~~~
Full Matching Job Title
(link)
Next Matching Job Title
....
~~~~

# Requirements
~~~
requests package

beautifulsoup4 package

python 3.x (tested for 3.5+ only)
~~~
# Usage
Set up with a cron job of your choice, I personally have mines run twice a day.

From the program's -h argument

~~~~
usage: scrape_site.py [-h] [--t] substr siteurl parsername

positional arguments:
  substr      substr to look for
  siteurl     url of site to scrape
  parsername  name of a parser to use

optional arguments:
  -h, --help  show this help message and exit
  --t         testing flag
~~~~

### Important
Create a config.py file with the variables:

username - smtp login username

password - smtp login password

emailname - target email to send to

host - host server

port - desired port

# TODO:

-Find a better alternative to doing if statements for the factory

-Create implementation that can integrate easily with amazon s3 and lambda
