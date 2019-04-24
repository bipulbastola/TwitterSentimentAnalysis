import twitter

# initialize api instance
twitter_api = twitter.Api(consumer_key='56YkT1Dw8FzWZgveLffz2eP1p',
                          consumer_secret='nAsmznOH2Fo9ha1yii1YKtWpL8MfbQrARIVBblauqMCToDJvrI',
                          access_token_key='1110107966919925760-yMbsWLYmnSLvbhqwDcBG1ZXlQOEnjo',
                          access_token_secret='LaEFIWRr7eLnMCI1KLbKW3LaEkhw7l56QuRTEnGqOdwA5')

# test authentication
print(twitter_api.VerifyCredentials())


"""Building Test Set Function
Tweets are downloaded  for the search term 
"""

def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count=100)

        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)

        return [{"text": status.text, "label": None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None


# Testing our Function
"""Showing four among all downloaded tweets"""

search_term = input("Enter a search keyword: ")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])


