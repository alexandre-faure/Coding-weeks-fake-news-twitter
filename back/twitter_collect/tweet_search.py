import back.twitter_collect.twitter_connection_setup as connect
import tweepy
from back.twitter_collect.twitter_connection_setup import twitter_setup
from back.tweet_analysis.url_analysis import url_to_id


def collect_whole(query, nb_tweets):
    """
    The function collect_whole searches tweets corresponding to keyword.

    The parameters used are
    :param query: this param represents the keyword of your interest and is of type str
    :param nb_tweets: this param represents the number of tweets collected and is of type int

    collect_whole returns a list of
    """
    api = twitter_setup()

    # Collect the tweets
    tweets = api.search_tweets(
        query, count=nb_tweets, tweet_mode="extended")

    liste = []

    # Get the content of each tweet
    for tweet in tweets:
        # we find the tweets and extract their full text (not default)
        try:
            tweet_content = tweet.retweeted_status.full_text
        except AttributeError:
            tweet_content = tweet.full_text
        name = tweet.user.name
        arobase = "@" + tweet.user.screen_name
        date = str(tweet.created_at)
        liste.append((name, arobase, date, tweet_content))
    # we return the list of analyzed tweets
    return liste


def collect_by_user(user_id, nb_tweets):
    """
    The function collect_by_user collects tweets from a certain user

    The parameters used are
    :param user_id: this param is the screen_name of the user of interest (@ of the author)
    :param nb_tweets: this param represents the number of tweets collected and is of type int

    collect_whole returns a list of tuples containing the username, the id of the user, the date and the content
    of the recent user's tweets
    """
    try:
        api = twitter_setup()

        # Collect the tweets
        statuses = api.user_timeline(
            screen_name=user_id, count=nb_tweets, exclude_replies=True)

        liste = []
        # Get the content of each tweet
        for tweet in statuses:
            # we found tweets
            tweet = api.get_status(tweet.id, tweet_mode="extended")
            try:
                tweet_content = tweet.retweeted_status.full_text
            except AttributeError:
                tweet_content = tweet.full_text
            name = tweet.user.name
            arobase = "@" + tweet.user.screen_name
            date = str(tweet.created_at)
            liste.append((name, arobase, date, tweet_content))
        if liste == []:
            # no tweets found
            user = api.get_user(screen_name=user_id)
            name = user.name
            arobase = '@' + user_id
            return ([(name, arobase, None, None)])
        return liste
    except:
        # user not found
        return [None]


def collect_replies(tweet_id, name, nb_replies):
    """ collect_replies collects a non-exhaustive list of tweets responding to a certain tweet

    The parameters used are
    :param tweet_id: this param is the id of the tweet of interestand is of type int
    :param name: this param is the screen_name of the author of the tweet and id of type str
    :param nb_replies: this param represents the number of tweets collected and is of type int

    collect_replies returns a list of tuples containing the username, the id of the user, the date 
    and the content of the tweet and a list of tuples containing the same informations about the replies. 
    """
    api = twitter_setup()

    # Collect the tweets
    tweets = api.search_tweets(
        "to:"+name, result_type='recent', count=nb_replies)
    replies = []

    # Get the content of each tweet
    for tweet in tweets:
        if (tweet.in_reply_to_status_id == tweet_id):
            status = api.get_status(tweet.id, tweet_mode="extended")
            tweet_content = status.full_text
            name = tweet.user.name
            arobase = "@" + tweet.user.screen_name
            date = str(tweet.created_at)
            replies.append((name, arobase, date, tweet_content))
    return replies


def collect_replies_to_candidate(name_candidate, nb_tweets, nb_replies):
    '''
    collect_replies_to_candidate gets the replies from multiple tweets published by a candidate

    :param name_candidate: this param represents the @ of the user and is a string
    :param nb_tweets: this param represents the number of tweets collected and is of type int
    :param nb_replies: this param represents the number of replies collected per tweet and is of type int

    get_replies_to_candidate returns a list of lists of type [user tweet, replies to the tweet] where user tweet
    and replies are tuples containing the username, the user id, the date and the content of the tweet.
    '''
    api = twitter_setup()

    # Collect the tweets
    tweets = api.search_tweets(
        "from:"+name_candidate, result_type='recent', count=nb_tweets)

    replies = []

    # Get the content of each tweet
    for tweet in tweets:
        # we extract the full content of the tweet
        tweet = api.get_status(tweet.id, tweet_mode="extended")
        try:
            tweet_content = tweet.retweeted_status.full_text
        except AttributeError:
            tweet_content = tweet.full_text
        name = tweet.user.name
        arobase = "@" + tweet.user.screen_name
        date = str(tweet.created_at)
        replies.append([(name, arobase, date, tweet_content), collect_replies(
            tweet.id, name_candidate, nb_replies)])
    return replies


def collect_tweet_from_url(url):
    '''
    collect_tweet_from_url gets relevant informations of the tweet from an url

    :param url: this param represents the url of the tweet and is a string

    collect_tweet_from_url returns a tuple containing the username the id of the user, the date and the content of the tweet
    '''
    # we catch the tweet id thanks to the url
    tweet_id = url_to_id(url)
    if tweet_id == None:
        print("The URL isn't valid")
        return (None, None, None, None)
    try:
        api = twitter_setup()
        tweet = api.get_status(tweet_id, tweet_mode="extended")
        try:
            tweet_content = tweet.retweeted_status.full_text
        except AttributeError:
            tweet_content = tweet.full_text
        name = tweet.user.name
        arobase = "@" + tweet.user.screen_name
        date = str(tweet.created_at)
        return (name, arobase, date, tweet_content)
    except:
        print("This tweet doesn't exist")
        return (None, None, None, None)
