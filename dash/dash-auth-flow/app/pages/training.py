import config
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import requests
from dash.dependencies import Output, Input
from server import app
from dash import no_update
from flask_login import logout_user, current_user
import json

login_alert = dbc.Alert(
    'User not logged in. Taking you to login.',
    color='danger'
)

location = dcc.Location(id='page1-url', refresh=True)
expertise_level = ['Novice', 'Advanced Beginner', 'Competent', 'Proficient', 'Expert']
labels = ['Benign', 'Likely Benign', 'VUS', 'Likely Pathogenic', 'Pathogenic']
expected_label = ''  # expected label (classification)of variant, to compare with user answer
selected_variant_id = ''  # selected variant id from the main table
# current_user = None


def api_request(api_route, method='GET', data=None, convert_to_df=True):
    """
    Perform a request to the given API route
    :param api_route: api route to send request (string)
    :param method: request method
    :param data: data to append to request (dict)
    :param convert_to_df: convert response (boolean). True=Pandas DataFrame, False=JSON
    :return: response (Pandas DataFrame/JSON)
    """
    if data is None:
        data = {}
    api_url = config.api_url + api_route

    try:
        response = None
        if method.upper() == 'GET':
            response = requests.get(api_url)
        elif method.upper() == 'POST':
            response = requests.post(api_url, data=data)
    except requests.exceptions.ConnectionError:
        print("ERROR: Couldn't connect to API. Please try again.")
        return 'error', "APIError"

    if response.status_code == 200:
        decoded_response = response.content.decode('utf-8')
        response_status = json.loads(decoded_response)['status']
        response_data = json.loads(decoded_response)['data']
        if convert_to_df:
            # data_df = pd.DataFrame.from_dict(json.loads(decoded_response), orient='index')
            response_data_df = pd.read_json(response_data)
            return response_status, response_data_df
        else:
            return response_status, response_data
    else:
        return 'error', 'None'


# API requests to be made when the page loads
api_route_variants = '/list_non_conflictive_variants'
status, df_variants = api_request(api_route_variants)  # load non-conflictive variants

api_route_labels = '/list_labels'
status_labels, df_labels = api_request(api_route_labels)  # load labels

def layout():
    return dbc.Row(
        dbc.Col(
            [
                location,
                html.H1('Stage 1 - Variant classification and expert training'),
                html.Br(),

                html.P(children='Please select a non-conflictive variant from the list:'),
                dash_table.DataTable(
                    id='datatable-interactivity',
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": True} for i in df_variants.columns
                    ],
                    data=df_variants.to_dict('records'),
                    # editable=True,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    # column_selectable="single",
                    row_selectable="single",
                    row_deletable=False,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current=0,
                    page_size=7,
                    # style_table={'overflowX': 'scroll'},
                    style_cell={
                        'overflow': 'hidden',
                        'textOverflow': 'ellipsis',
                        'maxWidth': 0,
                    },
                    # tooltip_data=[
                    #     {
                    #         column: {'value': str(value), 'type': 'markdown'}
                    #         for column, value in row.items()
                    #     } for row in df_variants.to_dict('rows')
                    # ],
                    # tooltip_duration=None,
                    style_header={
                        'backgroundColor': 'rgb(235, 235, 235)',
                        'fontWeight': 'bold'
                    },
                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(248, 248, 248)'
                        }
                    ],
                ),
                html.Div(id='datatable-interactivity-container'),
                html.Br(),
                dbc.Button(children=html.Span([html.I(className='fas fa-eye'), ' View details']), id='btn-view-details',
                           n_clicks=0, color='primary'),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div(
                    id='details-container',
                    children=[
                        html.H2(id='variant-info-title', children='Variant info', style={'font-weight': 'bold'}),

                        # basic info
                        html.H3('Basic'),
                        html.Div(id='variant-info-basic'),
                        # kaviar info
                        html.H3('Kaviar'),
                        html.Div(id='variant-info-kaviar'),
                        # gwava info
                        html.H3('Gwava'),
                        html.Div(id='variant-info-gwava'),
                        html.Br(),
                        html.Br(),

                        # user classification
                        html.H2('Your classification', style={'font-weight': 'bold'}),
                        html.P(
                            children='According to the information provided above, the classification of the variant '
                                     'corresponds to:'),
                        dcc.Dropdown(
                            id='combo-labels',
                            options=[{'label': i, 'value': i} for i in df_labels.label],
                            value=''
                        ),
                        html.Br(),
                        dbc.Button(
                            children=html.Span([html.I(className='fas fa-paper-plane'), ' Submit classification']),
                            id='btn-submit-classification', n_clicks=0, color='primary'),
                        html.Br(),
                        html.Br(),
                        dbc.Alert(id='msg-classification-feedback', children='', color='danger',
                                  style={'display': 'none'}),
                        html.Br(),
                        html.Br(),
                    ],
                    style={'display': 'none'},
                ),

            ], width=12)
    )
    # if current_user.is_authenticated:


def get_trigger_id():
    """
    Get the element id that triggered a callback
    :return: element id (string)
    """
    context = dash.callback_context
    if context.triggered:
        context_id = context.triggered[0]['prop_id'].split('.')[0]
    else:
        context_id = ''
    return context_id


@app.callback(
    [
        Output('variant-info-title', 'children'),
        Output('variant-info-basic', 'children'),
        Output('variant-info-kaviar', 'children'),
        Output('variant-info-gwava', 'children'),
        Output('details-container', 'style'),
        # Output('msg-classification-feedback', 'style'),
        # Output('btn-submit-classification', 'disabled')
    ],
    [
        Input('datatable-interactivity', 'selected_rows'),
        Input('btn-view-details', 'n_clicks'),
        # Input('btn-submit-classification', 'n_clicks'),
        # Input('combo-labels', 'value')
    ]
)
def view_variant(sel_rows, n_clicks):
    """
    Load and display information of the selected variant
    :param sel_rows: selected rows indices
    :param n_clicks: n clicks in the 'show info' button
    :return: [title, table, table, table, style]
    """
    context_id = get_trigger_id()
    print('element id:', context_id)

    if len(sel_rows) == 1 and context_id == 'btn-view-details':
        # avoid errors when no row is selected
        # get variant id from initially loaded dataframe
        global selected_variant_id
        selected_variant_id = df_variants.at[sel_rows[0], 'ID']
        print('\nSelected variant:', selected_variant_id)

        # request variant data to API
        route = '/get_variant'
        method = 'POST'
        data = {'variant_id': int(selected_variant_id)}
        status, df_selected_variant = api_request(route, method, data, True)

        global expected_label
        expected_label = df_selected_variant.at[0, 'InterVar_automated']
        # print('> expected label is:', expected_label, type(expected_label))

        # prepare variant info to display
        title = 'Info of variant: ' + str(selected_variant_id)

        basic_info = df_selected_variant.iloc[:, 0:8]
        # print('response: ', type(df_selected_variant), df_selected_variant)
        basic_table = dbc.Table.from_dataframe(basic_info, striped=True, bordered=True, hover=True)

        # kaviar_info = df_selected_variant[['Kaviar_AF', 'Kaviar_AC', 'Kaviar_AN']]
        kaviar_info = df_selected_variant.filter(like='Kaviar_')
        kaviar_table = dbc.Table.from_dataframe(kaviar_info, striped=True, bordered=True, hover=True)

        # gwava_info = df_selected_variant[['GWAVA_region_score', 'GWAVA_tss_score', 'GWAVA_unmatched_score']]
        gwava_info = df_selected_variant.filter(like='GWAVA_')
        gwava_table = dbc.Table.from_dataframe(gwava_info, striped=True, bordered=True, hover=True)

        return [title, basic_table, kaviar_table, gwava_table, {'display': 'block'}]
    else:
        raise dash.exceptions.PreventUpdate  # avoid update of elements


@app.callback(
    [
        Output('msg-classification-feedback', 'children'),
        Output('msg-classification-feedback', 'color'),
        Output('msg-classification-feedback', 'style')
    ],
    [
        Input('btn-submit-classification', 'n_clicks'),
        Input('combo-labels', 'value')
    ]
)
def show_classification_feedback(n_clicks, selected_label):
    """
    Show feedback based on user classification
    :param n_clicks:
    :param selected_label: selected value in classification combobox
    :return: [string, string, style]
    """
    context_id = get_trigger_id()

    if context_id == 'btn-submit-classification':
        global expected_label
        global selected_variant_id

        print('\tUser says:', selected_label, ', Expected:', expected_label)
        if selected_label.lower() == str(expected_label).lower():  # convert to lower to avoid lower/uppercase problems
            # User answer is correct
            is_correct = 1
        else:
            # User answer is wrong
            is_correct = 0

        # send classification data to API
        route = '/set_user_classification'
        method = 'POST'
        data = {'user_id': current_user.first, 'variant_id': selected_variant_id, 'label_id': selected_label,
                'is_correct': is_correct}
        status, response = api_request(route, method, data, False)

        if status == 'ok':
            if is_correct == 1:
                msg = "Well done. Congratulations!"
                color = "success"
            else:
                msg = [html.Span("Incorrect classification. The expected label was: "), html.Strong(expected_label)]
                color = "danger"
        else:
            if response == 'IntegrityError':
                # variant already classified
                msg = html.Span("You've already classified variant " + str(selected_variant_id))
                color = "warning"
            elif response == 'APIError':
                # API connection error
                msg = [html.Strong("API connection error:"), html.Span(" the classification could not be saved.")]
                color = "danger"
            else:
                msg = [html.Strong("Internal error:"), html.Span(" the classification could not be saved.")]
                color = "danger"

        style = {'display': 'block'}
    else:
        msg = ''
        color = ''
        style = {'display': 'none'}

    return [msg, color, style]
