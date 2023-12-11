import textblob
from back.twitter_collect.tweet_search import collect_whole


def emotion_by_topic(query, nb_tweets):
    """  
    The function emotion_by_topic returns the percentage of positive, negative or neutral tweets linked to a certain topic.
    It searches nb tweets relating to topic.

    The parameters used are 
    :param query: this param represents the topic of your interest and is of type str
    :param nb_tweets: this param represents the number of tweets collected and is of type int (WARNING: nb_tweets must be inferior to 100)

    emotion by topic returns a tuple (float, float, float, float)
    """
    # Collection of the tweets
    result = collect_whole(query, nb_tweets)
    nb_tweets = len(result)
    c = 0
    # Initialization of the parameters
    tot_pos, tot_neg, tot_neut, sub = 0, 0, 0, 0

    for tweet in result:
        (username, arobase, date, tweet_content) = tweet
        # Analyze sentiments for the tweet
        pol, sub1 = (textblob.TextBlob(tweet_content).correct()).sentiment
        # Handle positivity/negativity
        if pol < 0:
            tot_pos += 1
        elif pol > 0:
            tot_neg += 1
        else:
            tot_neut += 1
        # Handle subjectivity
        sub += sub1
        c += 1
    # return different scores
    return (100 * tot_pos / c, 100 * tot_neg / c, 100 * tot_neut / c, 100 * sub / c)


def emotion_by_tweet(tweet):
    """
    This function aims at providing the user with a number between 0 and 1 corresponding
    to the probability that the tweet submitted is reliable. We consider that a tweet is more likely 
    to be fake if it is subjective and negative. 
    The only parameter is 
    :param tweet: it is a string which represents the text contained in the tweet that we want to analyze
    emotion_by_tweet returns a value between 0 and 1 representing the probability that the tweet is reliable
    """
    pol, sub = (textblob.TextBlob(tweet).correct()).sentiment
    return (1 - (sub+0.1*abs(pol))/1.1)


# print(emotion_by_tweet(
#     "Vaccination against covid is responsible for many contaminations with aids."))
# print(emotion_by_tweet(
#     "Pokemon is out tomorrow ! Can't wait to try it out !"))
