from dash import Dash, dcc, html

# Get the README
file_readme = open("README.md", "r", encoding="utf-8")
contenu_readme = file_readme.read()

layout_tab_apropos = dcc.Markdown(contenu_readme, id="divReadme")
