## Twitter Stream using Python, Kafka and MongoDB
This application is a simplified model for extracting real time tweets and subsequent persistence in a Mongo DB database.

The application uses the Apache Kafka solution to stream the tweets collected by the python crawler that monitors tweets containing a specific word, at a time interval.

Afterwards, the messages available in the Kafka topic are consumed and stored in a Mongo DB database.

To access the Twitter API it is necessary to create a Twitter developer account and obtain the access keys.

## Como realizar o deploy da aplicação
1. Copy the fyles from this repo to a place where you want to run the application;
2. Create a .env file and define the following environment variables to acesse Twitter API and Mongo DB Database:
    * API_Key
    * API_Secret_key
    * access_token 
    * access_token_secret

    * mongopath 
    * mongouser 
    * password 

3. Open a terminal and run command "docker-compose up -d" to start Kafka
4. Open a new terminal and start kafka producer, with command "python stream_tweet.py"
5. Open a new terminal and start kafka consumeer, with command "python consume_tweet.py
6. In order to monitor the Kafka topic and its messages, access "localhost:9000" through our browser;
7. Messagens must now be saved on your Mongo DB Database
8. In order to modify the words to be searched, change the string value in the function api.search(), in stream_tweet.py

## License and Author info
MIT License

Copyright (c) 2021 Jeferson Machado Santos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.