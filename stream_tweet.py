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