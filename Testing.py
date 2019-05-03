from TwitterApi import twitterApi

# test authentication

print(twitterApi.twitter_api.VerifyCredentials())

"""Building Test Set Function
Tweets are downloaded  for the search term 
"""


def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitterApi.twitter_api.GetSearch(search_keyword, count=100)

        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)

        for status in tweets_fetched:
            print({"text": status.text})
            testdata = open("TestData.csv", "a")
            testdata.write(status.text)

        if (testdata):
            print("Successfully file created")

    except:
        print("Unfortunately, something went wrong..")
        return None


# Testing our Function


search_term = input("Enter a search keyword: ")
testDataSet = buildTestSet(search_term)

print(testDataSet)