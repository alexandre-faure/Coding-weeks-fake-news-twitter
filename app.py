"""Run this app with `python index.py` and
visit http://127.0.0.1:8050/ in your web browser."""

from dash import Dash, dcc, html, Input, Output, State

app = Dash(__name__)

app.config.suppress_callback_exceptions = True
