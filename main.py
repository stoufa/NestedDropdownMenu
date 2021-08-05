import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from nested_dropdown_menu import nested_dropdown_menu
from menu_structure import menu_structure

JQUERY_CDN_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# both simple and nested elements are dictionaries, the difference is: the
# simple elements have the 'href' attribute while the nested elements have a
# 'children' attribute; and both have the 'label' attribute


dropdown = nested_dropdown_menu(
    label='Menu',
    menu_structure=menu_structure
)


# __name__ will allow us to access the assets/ folder
# css files in assets/ will be automatically detected and loaded
app = dash.Dash(
    __name__,
    external_scripts=[JQUERY_CDN_URL],
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    html.Br(),
    html.H1(children='Nested Dropdown Test'),
    html.Br(),
    html.Div(id='output'),
    html.Br(),
    dropdown
], className='container')


@app.callback(
    Output('output', 'children'),
    [Input('url', 'pathname')]
)
def update_output(pathname):
    return html.Div([
        html.H3(f'You are on page {pathname}')
    ])


# setting the debug parameter/flag to True makes the webpage refresh
# automatically after every change of this file
app.run_server(debug=True)
