import tweepy
import requests
from random import randrange
import json
from datetime import datetime, timedelta
import time

with open("/Users/benar/Desktop/bot/data.Json", encoding='utf-8-sig', errors='ignore') as json_data:
     data = json.load(json_data, strict=False)

#print(s['DATE & DAY'])

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
print(y)
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
            
            
            
print(sc)
random_index = randrange(len(sc))

consumer_key='3wLLUBY8vhd3Xy0EIVHVbnIED'
consumer_secret='LPtsPXNL0PEW7bdx3ulnRi3zS42pVTzg51ZzzVrE1sgdKQrT2o'

access_token='1016913544036737025-lCTxlIw4EOr5aZqeThupq8IfaRajBu'
access_token_secret='jcfNhTs9psgvXsvlAw3e61i1xxOhkRfSnewO1Y7DlV1sH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets=api.user_timeline(screen_name="Benarjeekbn",count=1)
for info in tweets[:3]:
    s="Id:{}".format(info.id)
    print(id)


reply_tweet=[1388002514847473665]


while True:
    reply1_tweet = api.update_status(status="#IPL2021\n#"+sc[0]+"vs"+sc[1]+"\n"+"Winner: #"+sc[random_index], in_reply_to_status_id=reply_tweet[0],auto_populate_reply_metadata=True)
    reply_tweet[0]=reply1_tweet.id
    time.sleep(72000)


