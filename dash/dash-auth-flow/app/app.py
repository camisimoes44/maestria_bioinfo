# index page
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# from flask import redirect
from server import app, server
from flask_login import logout_user, current_user
import config

# app pages
from pages import (
    home,
    profile,
    classification,
    training,
)

# app authentication 
from pages.auth_pages import (
    login,
    register,
    forgot_password,
    change_password,
)


app.layout = html.Div(
    [
        dbc.Navbar(
            id="navbar",
            className="mb-5",
        ),
        html.Div(
            [
                dbc.Container(
                    id='page-content'
                )
            ]
        ),
        dcc.Location(id='base-url', refresh=False)
    ]
)


def generate_navbar(is_authenticated, user_name):
    """
    Generate the navigation bar depending if the user is authenticated or not
    :param is_authenticated: indicates if the user is authenticated (boolean)
    :param user_name: name of the user (string)
    :return: content of the navigation bar (Bootstrap Container)
    """
    navbar_items = [dbc.NavItem(dbc.NavLink('Login', id='user-action', href='/login'))]
    try:
        if is_authenticated:
            navbar_items = [
                dbc.NavItem(dbc.NavLink("Home", href="/home")),
                dbc.NavItem(dbc.NavLink("Training", href="/training")),
                dbc.NavItem(dbc.NavLink("Classification", href="/classification")),
                dbc.NavItem(dbc.NavLink(user_name, id='user-name', href='/profile')),
                dbc.NavItem(dbc.NavLink('Logout', id='user-action', href='/logout')),
            ]
    except:
        pass

    navbar_content = dbc.Container(
                [
                    dbc.NavbarBrand("Bioinformatics", href="/home"),
                    dbc.Nav(
                        navbar_items
                    )
                ]
            )

    return navbar_content


@app.callback(
    [Output('page-content', 'children'),
     Output('navbar', 'children')],
    [Input('base-url', 'pathname')])
def router(pathname):
    """
    routes to correct page based on pathname
    """
    print('routing to', pathname)
    # auth pages
    if pathname == '/login':
        if not current_user.is_authenticated:
            return login.layout(), generate_navbar(False, '')
    elif pathname == '/register':
        if not current_user.is_authenticated:
            return register.layout(), generate_navbar(False, '')
    elif pathname == '/change':
        if not current_user.is_authenticated:
            return change_password.layout(), generate_navbar(False, '')
    elif pathname == '/forgot':
        if not current_user.is_authenticated:
            return forgot_password.layout(), generate_navbar(False, '')
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()

    # app pages
    elif pathname == '/' or pathname == '/home' or pathname == '/home':
        if current_user.is_authenticated:
            return home.layout(), generate_navbar(True, current_user.user)
    elif pathname == '/profile' or pathname == '/profile':
        if current_user.is_authenticated:
            return profile.layout(), generate_navbar(True, current_user.user)
    elif pathname == '/classification' or pathname == '/classification':
        if current_user.is_authenticated:
            return classification.layout(), generate_navbar(True, current_user.user)
    elif pathname == '/training' or pathname == '/training':
        if current_user.is_authenticated:
            return training.layout(), generate_navbar(True, current_user.user)

    # DEFAULT LOGGED IN: /home
    if current_user.is_authenticated:
        return home.layout(), generate_navbar(True, current_user.user)

    # DEFAULT NOT LOGGED IN: /login
    return login.layout(), generate_navbar(False, '')


@app.callback(
    Output('user-name', 'children'),
    [Input('page-content', 'children')])
def profile_link(content):
    """
    returns a navbar link to the user profile if the user is authenticated
    """
    if current_user.is_authenticated:
        return html.Div(current_user.user)
    else:
        return ''


@app.callback(
    [Output('user-action', 'children'),
     Output('user-action', 'href')],
    [Input('page-content', 'children')])
def user_logout(input1):
    """
    returns a navbar link to /logout or /login, respectively, if the user is authenticated or not
    """
    if current_user.is_authenticated:
        return 'Logout', '/logout'
    else:
        return 'Login', '/login'


if __name__ == '__main__':
    app.run_server(host=config.server_ip, port=config.server_port, debug=config.debug)
