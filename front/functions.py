from back.twitter_collect.tweet_search import collect_tweet_from_url
import re
from dash import html
from datetime import datetime


def create_links(content, pattern):
    """create_links enables to replace the links in a text to html a components.
    :param content: text is of type str
    :param pattern: pattern to match is of type str
    return the content of a div with html.P object and html.A objects"""
    elements = []
    while content != "":
        search = re.search(pattern, content)
        if search == None:  # Plus de lien trouvé
            elements.append(content)
            content = ""
        else:  # Un lien est trouvé
            pos_beg, pos_end = search.span()
            elements.append(html.P(content[:pos_beg]))
            elements.append(
                html.A("lien externe", href=search.group(), target="_blank"))
            content = content[pos_end:]
    return elements


def clean_date(date):
    """Simplify the expression of a date
    :param date: date to the format YYYY-MM-JJ HH:MM:SS+ZZ:ZZ as a string
    The function returns a string to the format 'le JJ/MM/YY à HHhMM"""
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S%z")
    return date.strftime("le %d/%m/%Y à %Hh%M")


def create_gradient(reliability, category):
    """Function to generate a html.Div component to give a gradient of the reliability
    :param reliability: int between 0 and 100.
    :param category: str that depicts the nature of the element whose reliability is studied."""
    return (
        html.Div([
            html.Span([], id="spanReliable" + category,
                      className="spanReliable",
                      title="Fiable à " + str(int(reliability)) + "%",
                      style={'flex': int(reliability)}),
            html.Span([], id="spanFake" + category,
                      className="spanFake",
                      title="Fake news à " + str(int(100-reliability)) + "%",
                      style={'flex': int(100-reliability)})
        ], className="barReliability")
    )
