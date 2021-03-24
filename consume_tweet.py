from pymongo import MongoClient
import urllib.parse
from kafka import KafkaConsumer, KafkaProducer
import os
from json import loads
from dotenv import load_dotenv
load_dotenv()

mongouser = urllib.parse.quote_plus(os.getenv("mongouser"))
password = urllib.parse.quote_plus(os.getenv("password"))
mongopath = os.getenv("mongopath")

client = MongoClient('mongodb://%s:%s@%s'% (mongouser,password,mongopath))

db = client['tweet']
collection = db['consumed']

consumer = KafkaConsumer(
    'netflix',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    dic={'id':message}
    collection.insert_one(dic)
    print('{} added to {}'.format(message, collection))