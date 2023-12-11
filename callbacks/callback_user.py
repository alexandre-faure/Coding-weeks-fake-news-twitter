from app import app
from dash import Dash, dcc, html, Input, Output, State
from back.twitter_collect.tweet_search import collect_tweet_from_url
from back.twitter_collect.tweet_search import collect_by_user
from back.twitter_collect.tweet_search import collect_whole
from front.functions import create_links, clean_date, create_gradient
from back.tweet_analysis.ia_analysis import user_reliability
from front.text_content.text_fr import *


@app.callback(
    Output("divApercuUser", "children"),
    Output("divAnalyseUser", "children"),

    Input("buttonValiderUtilisateur", "n_clicks"),
    State('inputRechercherutilisateur', 'value')
)
def update_user_fields(n_clicks, username_at):
    data = collect_by_user(username_at, 5)
    if username_at == "":  # No user searched
        return (html.P([ERROR_NO_USER], className="adviceText infoText"),
                html.P([ERROR_NO_USER],
                       className="adviceText infoText"))
    elif data == [None]:  # The user doesn't exist
        return (html.P([ERROR_INVALID_USER], className="errorText infoText"),
                html.P([ERROR_INVALID_USER], className="errorText infoText"))
    else:
        # No tweet by this user
        if len(data) == 1 and len(data[0]) == 4 and data[0][2] is None and data[0][3] is None:
            return (
                html.Div([
                    html.P([data[0][0]],
                           id="username_user",
                           className="apercuTweetUsername1"),
                    html.P([data[0][1]],
                           id="username_at_user",
                           className="apercuTweetUserAt1"),
                    html.P([" Cet utilisateur n'a publié aucun tweet à ce jour. "])
                ], className="apercuProfil"),

                html.P([" Ce compte n'a publié aucun tweet et ne peut donc être évalué. "]))
        else:
            # Generation of the tweets preview
            res = []
            res.append(html.Br())
            i = 0
            for tweet in data:
                res.append(
                    html.Div([
                        html.P([tweet[0]],
                               id="apercuTweetUsername_user"+str(i),
                               className="apercuTweetUsername"),
                        html.P([tweet[1]],
                               id="apercuTweetUserAt_user"+str(i),
                               className="apercuTweetUserAt"),
                        html.P([clean_date(tweet[2])],
                               id="apercuTweetDate_user"+str(i),
                               className="apercuTweetDate"),
                        html.Div(create_links(tweet[3], r"https://t\.co/\S+"),
                                 id="apercuTweetContent_user"+str(i),
                                 className="apercuTweetContent")
                    ], className="apercuTweet")
                )
                i += 1
            # Reliability of the user
            reliability = user_reliability(username_at)
            return (
                html.Div([
                    html.P([data[0][0]],
                           id="username_user"),
                    html.P([data[0][1]],
                           id="username_at_user"),
                    html.Div(res)
                ], className="apercuProfil"),

                html.Div([
                    html.P(INTRO_RESULTS_SENTENCE_USER),
                    html.P(RESULTS_SENTENCE_USER + str(reliability) + "%.",
                           className="sentence_result"),
                    create_gradient(reliability, "User"),
                    html.P(EXPLANATIONS_RELIABILITY_RESULTS)
                ], className="divResults"))
