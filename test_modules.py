import tweepy

import back.tweet_analysis.tweet_emotions as emo

import back.tweet_analysis.url_analysis as url

import back.twitter_collect.twitter_connection_setup as setup

import back.twitter_collect.tweet_search as query

import back.tweet_analysis.ia_analysis as ai

import back.twitter_artificial_intelligence.fake_news_detector as ia
# on teste le package tweet_analysis

# on teste les pourcentages des différentes données (tweet_emotions)
(positivite, negativite, neutralite, subjectivite) = emo.emotion_by_topic("Trump", 10)
assert positivite <= 100 and positivite >= 0
assert negativite <= 100 and negativite >= 0
assert neutralite <= 100 and neutralite >= 0
assert subjectivite <= 100 and subjectivite >= 0
assert (positivite + negativite + neutralite == 100)

# on teste la fonction url_to_id

assert (url.url_to_id(
    "https://twitter.com/Arkunir/status/1591790067173167105") == 1591790067173167105)

assert ((url.url_to_id("jjbgcviqbdfwvuilsdjfglvqdhorvqbreoe")) == None)

# on teste le package twitter_collect

# on teste le type Status (twitter_connection_setup)

assert isinstance(setup.twitter_setup(), tweepy.API)

# on teste les fonctions de requête (tweet_search)

# requête pour les posts sur un sujet

liste = query.collect_whole("Trump", 10)

assert isinstance(liste, list)

for tweet in liste:
    assert isinstance(tweet, tuple)
    (a, b, c, d) = tweet
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert isinstance(c, str)
    assert isinstance(d, str)

# requête pour les posts d'un utilisateur

liste2 = query.collect_by_user("JoeBiden", 10)

assert isinstance(liste2, list)

a = query.collect_by_user("elisa21rssl", 2)
assert (isinstance(a, list))
assert (isinstance(a[0], tuple))

b = query.collect_by_user("fgqidbqdmbqdbjwon", 2)
assert (isinstance(b, list))
assert (b[0] == None)

for tweet in liste2:
    (a, b, c, d) = tweet
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert isinstance(c, str)
    assert isinstance(d, str)

# requête pour les réponses à un tweet

# /!\ choisir un tweet récent sinon on ne le récupèrera pas

liste3 = query.collect_replies(1592872787676631040, "DudespostingWs", 10)

assert isinstance(liste3, list)

for tweet in liste3:
    assert isinstance(tweet, tuple)

# requête pour les réponses à un utilisateur

liste4 = query.collect_replies_to_candidate("JoeBiden", 10, 10)

assert isinstance(liste4, list)

for tweet in liste4:
    origin = tweet[0]
    isinstance(origin, tweepy.models.Status)
    for replies in tweet[1]:
        assert isinstance(replies, tuple)
        (a, b, c, d) = replies
        assert isinstance(a, str)
        assert isinstance(b, str)
        assert isinstance(c, str)
        assert isinstance(d, str)

# requête pour les informations utiles d'un tweet connaissant son url

(a, b, c, d) = query.collect_tweet_from_url(
    "https://twitter.com/Xavier75/status/1591734188214190080")

assert isinstance(a, str)
assert isinstance(b, str)
assert isinstance(c, str)
assert isinstance(d, str)

assert query.collect_tweet_from_url(
    "fjhhglqmbciblvioy") == (None, None, None, None)

assert query.collect_tweet_from_url(
    "https://twitter.com/EmmanuelMacron/status/159285942954400328381267931255632") == (None, None, None, None)

# on teste les fonctions ia

x = ai.user_reliability("JoeBiden")
assert (isinstance(x, int))
assert (x > -1)
assert (x < 101)

y = ai.user_reliability("hgfqhbfqhbduifrflbcRQE")
assert (y == None)

q = y = ai.user_reliability("elisa21rssl")
assert (y == None)
z = ai.keyword_reliability("potato")
assert (isinstance(z, int))
assert (z > -1)
assert (z < 101)

w = ai.keyword_reliability("hflhdbfblqdbbhvjqhrbuqdkc")
assert (w == None)

assert (isinstance(ia.get_prediction("Bonjour Gautier Bonjour"), str))
assert (isinstance(ia.get_prediction("Bonjour Gautier Bonjour", False), int))
