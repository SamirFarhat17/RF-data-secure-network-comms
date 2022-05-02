import requests
import os
import json

def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

# Create URL and query keyword, number of results, the author, and date created
def create_url(keyword, max_results=10):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': keyword,'max_results': max_results,'tweet.fields': 'author_id,created_at'}

    return (search_url, query_params)

def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print("Endpont Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# Set up environment with authentication code
# Get number of tweets and keyword to search
print("Enter number of recent tweets to grab (minimum 10, maximum 100)")
max_results = input()
print("Please enter a keyword to find a message to send:")
keyword = input()
print("\n")

print("Please enter your Bearer Authentication code")
# Token must be a twitter API bearer token or else program will not run
intoken = input()
os.environ['TOKEN'] = str(intoken)

# Authenticate bearer token
bearer_token = auth()
# Create header with bearer token
headers = create_headers(bearer_token);
# Generate URL with inputs
url = create_url(keyword, max_results);
# Connect to endpoint to grab URL and tweets
json_response = connect_to_endpoint(url[0], headers, url[1])
# Get tweet portion of output response
[attribute,value]=json_response.items()
outresponse=(attribute[1])

tweetnum = 1
textfile = "plain.txt"
with open(textfile, 'w') as f:
    # print output of tweets
    f.write("\n")
    for tweets in outresponse:
        startline = "#####tweet" + str(tweetnum) + "#####"
        f.write(startline)
        f.write("\n")
        f.write(tweets['author_id'])
        f.write("\n")
        f.write(tweets['created_at'])
        f.write("\n")
        f.write(tweets['text'])
        f.write("\n")
        # If there is a file in the tweet, print on separate line, else print none
        haspic = tweets['text'].find('https://')
        if haspic == -1:
            f.write("none")
        else:
            pictext = tweets['text'][haspic:]
            pictext.split(" ", 1)
            f.write(pictext)
        # increment tweet number
        f.write("\n")
        tweetnum += 1
        
