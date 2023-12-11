from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
from front.tabs.tab_tweet import layout_tab1
from front.tabs.tab_user import layout_tab2
from front.tabs.tab_keyword import layout_tab3
from front.tabs.tab_apropos import layout_tab_apropos
import callbacks.callback_tweets
import callbacks.callback_user
import callbacks.callback_keyword
from app import app
from front.text_content.text_fr import *

app.layout = html.Div([
    html.Div([
        html.H1(TITLE_APP),
        html.P(SUBTITLE_APP)
    ], id="divTitle"),

    html.Div([
        html.Div([
            html.A(TAB_TWEET_TITLE, href="#tab1"),
            layout_tab1
        ], id="tab1"),



        html.Div([
            html.A(TAB_USER_TITLE, href="#tab2"),
            layout_tab2
        ], id="tab2"),



        html.Div([
            html.A(TAB_KEYWORD_TITLE, href="#tab3"),
            layout_tab3
        ], id="tab3"),



        html.Div([
            html.A(TAB_APROPOS_TITLE, href="#tabAPropos"),
            html.Div([
                layout_tab_apropos
            ], id="containerReadme")
        ], id="tabAPropos")


    ], className="tabs")
])


if __name__ == '__main__':
    app.run_server(debug=True)
