"""
The role of this script is to test the different twitter API
subscription models, namely: Search Tweets: 30-Days, Search Tweets: Full Archive,
Account Activity API


To set up premium API access, set up a development environment e.g staging, prod
for each of the subscription endpoints ie 30-day search, full archive search,
account activity

When authenticating with premium, we can only use the consumer tokens or the bearer token


Additional info:
https://developer.twitter.com/en/docs/twitter-api/premium/search-api/api-reference/premium-search
"""

import requests
import os
import json
from datetime import datetime

bearer_token = os.environ.get("BEARER_TOKEN")


# FULL ARCHIVE SEARCH
search_url = "https://api.twitter.com/1.1/tweets/search/fullarchive/staging.json"
# 30-DAY ENDPOINT
# search_url = "https://api.twitter.com/1.1/tweets/search/30day/staging.json"

# query parameters
query_params = {'query': 'from:technicollins', 'since_id': None, 'fromDate': '200612220000', 'maxResults': 100}
# if you don't specify the fromDate, only tweets from the last 30 days will be returned
# set max results to 500 if using the paid premium tiers


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)

    tweets = json_response['results']

    for tweet in tweets:
    	print(tweet['text'])


if __name__ == "__main__":
    main()
