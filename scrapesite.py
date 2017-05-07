from bs4 import BeautifulSoup
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
parser.add_argument("--t", help="testing flag", action="store_true")
args = parser.parse_args()

if args.t:
    print('testing')


url = args.siteurl
r = requests.get("https://"+url)
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

#look through all h5 tags, determine validity
#this is the part to modify if you want to make this work for not twitch
for i in soup.find_all("h5"):
    if args.substr.lower() in i.string.lower():
        jobname = i.string
        p = i.find_parent("a")
        if args.t:
            print(p)
        joblink = p.get('href')

        if joblink not in senturls:
            senturls.add(joblink)
            msg += jobname + '\n' + joblink + '\n'

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
