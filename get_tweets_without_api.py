# snscrape is a scraper for social networking services (SNS). 
# It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = " "

#scrapes only 100 tweets
tweets = []
limits = 10

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    #print(vars(tweet))
    #break
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

df.to_csv('tweets.csv')
