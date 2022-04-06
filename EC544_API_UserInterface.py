import requests
import os
import json
import csv

import pandas as pd

def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, max_results=10):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': keyword,'max_results': max_results,'tweet.fields': 'author_id'}

    return (search_url, query_params)

def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print("Endpont Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    else:
        print("Successful authenticaiton.")
        print("\n")
    return response.json()

# Set up environment with authentication code
print("Welcome to EC544 Team 3 Project")
print("Please enter a keyword to find a message to send:")
keyword = input()
print("\n")

print("Please enter your Bearer Authentication code")
# Token must be a twitter API bearer token or else program will not run
intoken = input()
os.environ['TOKEN'] = str(intoken)

bearer_token = auth()
headers = create_headers(bearer_token);
max_results = 100 #randomly generated result number to grab at least one tweet that is not a RT or reply
url = create_url(keyword, max_results);
json_response = connect_to_endpoint(url[0], headers, url[1])
[attribute,value]=json_response.items()
outresponse=(attribute[1])

encryptmsg = ""
msgauthor = ""
for tweets in outresponse:
    # each response will have an author_id, text
    currenttweet=tweets['text']
    first1str=currenttweet[0]
    first2str=first1str+currenttweet[1]
    isretweet=first2str=="RT"
    isreply=first1str=="@"
    if isretweet==0:
        if isreply==0:
            print("Message to Encrypt:")
            print(currenttweet)
            encryptmsg = currenttweet
            msgauthor = tweets['author_id']
            break;
