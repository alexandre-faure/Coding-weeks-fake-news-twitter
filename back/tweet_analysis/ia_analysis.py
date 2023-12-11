from back.twitter_collect.tweet_search import collect_by_user
from back.twitter_collect.tweet_search import collect_whole
from back.tweet_analysis.tweet_emotions import emotion_by_tweet


def user_reliability(user_id):
    ''' 
    The function user_reliability aims to give a score of reliability given a certain @

    :param user_id: this param represents the @ of the user and is of type string

    user_reliability returns an int between 0 and 100 representing reliability
    '''
    try:
        # we found the user and he has tweets
        score = 0
        i = 0
        tweets = collect_by_user(user_id, 10)
        if tweets[0] == None:
            # if the user is suspended/doesn't exist!
            print("User not found")
            return None
        for tweet in tweets:
            (name, arobase, date, tweet_content) = tweet
            score += 1-emotion_by_tweet(tweet_content)
            i += 1
        # we return a score
        return (int(100*score/i))
    except TypeError:
        # we didn't find any tweet!
        print("No tweet found")
        return (None)


def keyword_reliability(keyword):
    ''' 
    The function keyword_reliability aims to give a score of reliability given a certain keyword

    :param keyword: this param represents the keyword and is of type string

    key_word_reliability returns an int between 0 and 100 representing reliability related to this keyword
    '''
    try:
        # we found tweets
        score = 0
        i = 0
        tweets = collect_whole(keyword, 10)
        for tweet in tweets:
            # we analyze them
            (name, arobase, date, tweet_content) = tweet
            score += emotion_by_tweet(tweet_content)
            i += 1
        # we return a score
        return (int(100*score/i))
    except ZeroDivisionError:
        # we didn't find any related tweet
        print("No tweet found")
        return (None)
