from app import app
from dash import Dash, dcc, html, Input, Output, State
from back.twitter_collect.tweet_search import collect_tweet_from_url
from back.twitter_collect.tweet_search import collect_by_user
from back.twitter_collect.tweet_search import collect_whole
from front.functions import create_links, clean_date, create_gradient
from back.tweet_analysis.ia_analysis import keyword_reliability
from front.text_content.text_fr import *


@app.callback(
    Output("divApercuKeyword", "children"),
    Output("divAnalyseKeyword", "children"),

    Input("buttonValiderMotClé", "n_clicks"),
    State('inputKeyword', 'value')
)
def update_user_fields(n_clicks, keyword):
    if keyword == "":  # No keyword in the input
        return (html.P([ERROR_NO_KEYWORD], className="adviceText infoText"),
                html.P([ERROR_NO_KEYWORD], className="adviceText infoText"))
    try:
        # Generation of the tweets preview
        data = collect_whole(keyword, 5)
        res, i = [], 0
        for tweet in data:
            res.append(
                html.Div([
                    html.P([tweet[0]],
                           id="apercuTweetUsername_keyword"+str(i),
                           className="apercuTweetUsername"),
                    html.P([tweet[1]],
                           id="apercuTweetUserAt_keyword"+str(i),
                           className="apercuTweetUserAt"),
                    html.P([clean_date(tweet[2])],
                           id="apercuTweetDate_keyword"+str(i),
                           className="apercuTweetDate"),
                    html.Div(create_links(tweet[3], r"https://t\.co/\S+"),
                             id="apercuTweetContent_keyword"+str(i),
                             className="apercuTweetContent")
                ], className="apercuTweet")
            )
            i += 1
        # Get reliability of the keyword
        reliability = keyword_reliability(keyword)
        return (
            res,

            html.Div([
                html.P(INTRO_RESULTS_SENTENCE_KEYWORD),
                html.P(RESULTS_SENTENCE_KEYWORD + str(reliability) + "%.",
                       className="sentence_result"),
                create_gradient(reliability, "Keyword"),
                html.P(EXPLANATIONS_RELIABILITY_RESULTS)
            ], className="divResults"))
        return res
    except Exception as e:
        return (html.P([UNKNOWN_ERROR+" "+e], className="errorText infoText"),
                html.P([UNKNOWN_ERROR+" "+e], className="errorText infoText"))
