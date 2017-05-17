from bs4 import BeautifulSoup
from parserfactory import ParserFactory
import requests
import argparse
import config
import pickle
import time
import smtplib

#argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("substr", help="substr to look for")
parser.add_argument("siteurl", help="url of site to scrape")
parser.add_argument("parsername", help="name of a parser to use")
parser.add_argument("--t", help="testing flag", action="store_true")
args = parser.parse_args()

if args.t:
    print('testing')


url = args.siteurl

if "https://" not in url:
    url = "https://" + url

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")
msg = ''

#if file doesnt exist, initialize with empty file
try:
    with open('senturls' + args.substr + '.pickle', 'rb') as handle:
        senturls = pickle.load(handle)
except FileNotFoundError:
    if args.t:
        print('FileNotFoundError caught')
    senturls = set()

factory = ParserFactory()
p = factory.build(args.parsername, soup, senturls, args.substr, args.t)

msg = p.parse()

#dump back into pickle file
with open('senturls' + args.substr + '.pickle', 'wb') as handle:
    pickle.dump(senturls, handle, pickle.HIGHEST_PROTOCOL)

#smtp request
#if testing, will not actually send but will try to do all other steps
if msg != '':
    msg += 'Completed ' + time.strftime("%H:%M:%S") + '\n'
    if args.t:
        print("sending")
    s = smtplib.SMTP(config.host, config.port)
    s.starttls()
    s.login(config.username, config.password)
    if not args.t:
        s.sendmail(config.emailname, config.emailname, msg)
    s.quit()
