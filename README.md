# jobnotif
Quick and dirty python script that uses beautifulsoup to scrape a url and send an email through smtp if a job matching a substring is found.
Wanted to keep track of Twitch's internship opportunities but no option to automatically email is available.
Keeps track of duplicate jobs with a set stored using pickle.

Output email is in the form of:

Full Matching Job Title
(link)
Next Matching Job Title
....

(probably doesn't work for many sites generically, designed for twitch's job site specifically, but feel free to try, probably don't need to change much to make it work)

# Requirements
requests package

beautifulsoup4 package

python 3.x (tested for 3.5+ only)

# Usage
Set up with a cron job of your choice, I personally have mines run twice a day.

From the program's -h argument

~~~~
usage: scrapesite.py [-h] [--t] substr siteurl

positional arguments:
  substr      substr to look for
  siteurl     url of site to scrape

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

