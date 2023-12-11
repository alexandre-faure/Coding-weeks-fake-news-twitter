from dash import Dash, dcc, html
from front.text_content.text_fr import *

layout_tab2 = html.Div([
    html.Div([
        html.Div([

            html.H2(SEARCH_USER_TITLE),
            dcc.Input(
                id='inputRechercherutilisateur',
                placeholder=PLACEHOLDER_USER_INPUT,
                type="text",
                value=""
            ),
            html.Button(
                'Valider', id='buttonValiderUtilisateur', n_clicks=0)

        ], className="flexElement flexTop"),
        html.Div([

            html.H2(RELIABILITY_USER_TITLE),
            html.Div([], id="divAnalyseUser")

        ], className="flexElement flexBottom")
    ], className="flexContainerCol flexContainer flexLeft flexElement"),
    html.Div([
        html.H2(PREVIEW_USER_TITLE),
        html.Div([], id="divApercuUser",
                 className="divApercu")
    ], className="flexRight flexElement",
        style={"height": "fit-content"})
], className="flexContainer")
