from dash import Dash, dcc, html
from front.text_content.text_fr import *

layout_tab1 = html.Div([
    html.Div([
        html.Div([

            html.H2(SEARCH_TWEET_TITLE),
            dcc.Input(
                id='inputRechercherTweet',
                placeholder=PLACEHOLDER_TWEET_INPUT,
                type="text",
                value=""
            ),
            html.Button(
                'Valider', id='buttonValiderTweet', n_clicks=0)

        ], className="flexElement flexTop"),
        html.Div([

            html.H2(RELIABILITY_TWEET_TITLE),
            html.Div([], id="divAnalyseTweet")

        ], className="flexElement flexBottom")
    ], className="flexContainerCol flexContainer flexLeft flexElement"),
    html.Div([

        html.H2(PREVIEW_TWEET_TITLE),
        html.Div([], id="divApercuTweet",
                 className="divApercu")

    ], className="flexRight flexElement",
        style={"height": "fit-content"})
], className="flexContainer")
