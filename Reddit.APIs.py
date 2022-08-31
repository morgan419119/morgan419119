import requests
import pandas as pd
import os
import json
import csv

from requests.api import head

url = "https://tradestie.com/api/v1/apps/reddit"


headers = {
    'Accept': 'applications/json',
    'Content-Type': 'application/json'
}
response = requests.request("GET", url,headers=headers,data={})
myjson = response.json()

print(myjson)

ourdata =[]
csvheader = ['NO_OF_COMMENTS', 'SENTIMENT', 'SENTIMENT_SCORE','TICKER']


for x in myjson['data']:
    listing = [x['no_of_comments'],x['sentiment'],x['sentiment_score'],x['ticker']]
    ourdata.append(listing)

print(ourdata)

with open('temp.csv','w',enconding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(csvheader)
    writer.writerrows(ourdata)
    
print('done')























