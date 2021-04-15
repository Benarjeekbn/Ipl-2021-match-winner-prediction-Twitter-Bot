import tweepy
import requests
from random import randrange
import json
from datetime import datetime, timedelta
import time

with open("data.Json", encoding='utf-8-sig', errors='ignore') as json_data:
     data = json.load(json_data, strict=False)


l={'Royal Challengers Bangalore':'RCB',
   'Chennai Super Kings':'CSK',
   'Delhi Capitals':'DC',
   'Mumbai Indians':'MI',
   'Rajasthan Royals':'RR',
   'Punjab Kings':'PBKS',
   'Kolkata Knight Riders':'KKR',
   'Sunrisers Hyderabad':'SRH'
   }
x = datetime.now()

y=x.strftime("%B")+" "+x.strftime("%d")+", "+x.strftime("%A")

for i in range(1,61):
    s=data["Table 1"][i]
    p=s["DATE & DAY"]
    if p==y:
        match=s["MATCH"]
        break

teams=match.split(' vs ')
sc=[]
for k,v in l.items():
    for i in teams:
        if i==k:
            sc.append(v)
            
            
            

random_index = randrange(len(sc))

consumer_key='xxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

access_token='xxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

reply_tweet=[xxxx]
while True:
    reply1_tweet = api.update_status(status="#IPL2021\n#"+sc[0]+"vs"+sc[1]+"\n"+"Winner: #"+sc[random_index], 
                                 in_reply_to_status_id=reply_tweet[0], 
                                 auto_populate_reply_metadata=True)
    reply_tweet[0]=reply1_tweet.id
    time.sleep(72000)
