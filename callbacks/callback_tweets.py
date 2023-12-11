from app import app
from dash import Dash, dcc, html, Input, Output, State
from back.twitter_collect.tweet_search import collect_tweet_from_url
import time
import re
from datetime import datetime
from front.functions import create_links, clean_date, create_gradient
from back.tweet_analysis.tweet_emotions import emotion_by_tweet
import pandas as pd
from front.text_content.text_fr import *


@app.callback(
    Output("divApercuTweet", "children"),
    Output("divAnalyseTweet", "children"),
    Input('buttonValiderTweet', 'n_clicks'),
    State('inputRechercherTweet', 'value')
)
def update_tweet_fields(n_clicks, url):
    username, userat, date, content = collect_tweet_from_url(url)
    if url == "":
        return (html.P([ERROR_NO_TWEET], className="adviceText infoText"),
                html.P([ERROR_NO_TWEET], className="adviceText infoText"))
    elif (username, userat, date, content) == (None, None, None, None):
        return (html.P([ERROR_INVALID_TWEET], className="errorText infoText"),
                html.P([ERROR_INVALID_TWEET], className="errorText infoText"))
    else:
        reliability = round(100 * (1 - emotion_by_tweet(content)))
        print(reliability)
        return (
            html.Div([
                html.P([username],
                       id="apercuTweetUsername_tweet",
                       className="apercuTweetUsername"),
                html.P([userat],
                       id="apercuTweetUserAt_tweet",
                       className="apercuTweetUserAt"),
                html.P([clean_date(date)],
                       id="apercuTweetDate_tweet",
                       className="apercuTweetDate"),
                html.Div(create_links(content, r"https://t\.co/\S+"),
                     id="apercuTweetContent_tweet",
                     className="apercuTweetContent")
            ], className="apercuTweet"),

            html.Div([
                html.P(INTRO_RESULTS_SENTENCE_TWEET),
                html.P(RESULTS_SENTENCE_TWEET + str(reliability) + "%.",
                       className="sentence_result"),
                create_gradient(reliability, "Tweet"),
                html.P(EXPLANATIONS_RELIABILITY_RESULTS)
            ], className="divResults")
        )
