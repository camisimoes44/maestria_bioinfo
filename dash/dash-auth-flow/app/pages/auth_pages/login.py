import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import no_update

from flask_login import login_user, current_user

from server import app, User
import common

success_alert = dbc.Alert(
    'Logged in successfully. Taking you home!',
    color='success',
    dismissable=True
)
failure_alert = dbc.Alert(
    'Login unsuccessful. Please try again.',
    color='danger',
    dismissable=True
)
already_login_alert = dbc.Alert(
    'User already logged in. Taking you home!',
    color='warning',
    dismissable=True
)


def layout():
    return dbc.Row(
        dbc.Col(
            [
                dcc.Location(id='login-url', refresh=True, pathname='/login'),
                html.Div(id='login-trigger', style=dict(display='none')),
                html.Div(id='login-alert'),
                dbc.FormGroup(
                    [
                        # dbc.Alert('Try test@test.com / test', color='info', dismissable=True),
                        html.H3('Login'),
                        html.P('Please enter your credentials to access the platform'),

                        dbc.Input(id='login-username', autoFocus=True),
                        dbc.FormText('Username'),

                        html.Br(),
                        dbc.Input(id='login-password', type='password'),
                        dbc.FormText('Password'),

                        html.Br(),
                        dbc.Button(
                            children=html.Span([html.I(className='fas fa-paper-plane'), ' Submit']),
                            color='primary',
                            id='login-button'),
                        # dbc.FormText(id='output-state')

                        # html.Br(),
                        # html.Br(),
                        # dcc.Link('Register', href='/register'),
                        # html.Br(),
                        # dcc.Link('Forgot Password?', href='/forgot')
                    ]
                )
            ],
            width=6
        )
    )


@app.callback(
    [Output('login-url', 'pathname'),
     Output('login-alert', 'children')],
    [Input('login-button', 'n_clicks')],
    [State('login-username', 'value'),
     State('login-password', 'value')]
)
def login_success(n_clicks, username, password):
    """
    logs in the user
    """
    if n_clicks > 0:
        # send login data to API
        route = '/users/login'
        method = 'POST'
        data = {'user': username, 'password': password}
        status, response = common.api_request(route, method, data, False)

        if status == 'ok':
            user = User(response)
            # print(user.id, user.name, '-->', user.is_active, user.is_authenticated, user.is_anonymous)
            login_state = login_user(user)
            print('>>> login_user:', user.user, ', logged in:',  str(login_state))

            if login_state:
                return '/home', success_alert
            else:
                return no_update, failure_alert
        else:
            return no_update, failure_alert
    else:
        return no_update, ''
