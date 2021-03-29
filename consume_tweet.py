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