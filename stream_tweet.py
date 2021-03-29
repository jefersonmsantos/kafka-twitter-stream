#MIT License

#Copyright (c) 2021 Jeferson Machado Santos

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from kafka import KafkaConsumer, KafkaProducer
import tweepy
import time
import os
from dotenv import load_dotenv
load_dotenv()

API_Key =os.getenv("API_Key")
API_Secret_key =os.getenv("API_Secret_key")

access_token =os.getenv("access_token")
access_token_secret =os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(API_Key, API_Secret_key)
auth.set_access_token(access_token, access_token_secret)

#construir instância api
api = tweepy.API(auth)


producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = 'netflix'

def get_twitter_data():
    res = api.search("#netflix")
    for i in res:
        record=''
        record+= str(i.user.id_str)

        producer.send(topic_name,str.encode(record))

get_twitter_data()

def periodic_work(interval):
    while(True):
        get_twitter_data()
        time.sleep(interval)

periodic_work(60*0.1)