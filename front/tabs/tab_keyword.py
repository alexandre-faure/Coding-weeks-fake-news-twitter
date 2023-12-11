from dash import Dash, dcc, html
from front.text_content.text_fr import *

layout_tab3 = html.Div([
    html.Div([
        html.Div([

            html.H2(SEARCH_TWEET_TITLE),
            dcc.Input(
                id='inputKeyword',
                placeholder=PLACEHOLDER_KEYWORD_INPUT,
                type="text",
                value=""
            ),
            html.Button(
                'Valider', id='buttonValiderMotClé', n_clicks=0)

        ], className="flexElement flexTop"),
        html.Div([

            html.H2(RELIABILITY_KEYWORD_TITLE),
            html.Div([], id="divAnalyseKeyword")

        ], className="flexElement flexBottom")
    ], className="flexContainerCol flexContainer flexLeft flexElement"),
    html.Div([

        html.H2(PREVIEW_KEYWORD_TITLE),
        html.Div([], id="divApercuKeyword",
                 className="divApercu")

    ], className="flexRight flexElement",
        style={"height": "fit-content"})
], className="flexContainer")
