import config
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import requests
from dash.dependencies import Output, Input
from server import app

login_alert = dbc.Alert(
    'User not logged in. Taking you to login.',
    color='danger'
)

location = dcc.Location(id='page1-url', refresh=True)
expertise_level = ['Novice', 'Advanced Beginner', 'Competent', 'Proficient', 'Expert']
labels = ['Benign', 'Likely Benign', 'VUS', 'Likely Pathogenic', 'Pathogenic']
input_csv = "static/genomic.csv"
expected_label = ''


def request_to_api(api_route, data=None, convert_to_df=True):
    """
    Perform a request to the API
    :param api_route: api route to request (string)
    :param data: data to append to request (dict)
    :param convert_to_df: convert response, True=Pandas DataFrame, False=JSON (boolean)
    :return: response (Pandas DataFrame)
    """
    if data is None:
        data = {}
    api_url = config.api_url + api_route
    response = requests.post(api_url, data=data)
    if response.status_code == 200:
        decoded_response = response.content.decode('utf-8')
        if convert_to_df:
            data_df = pd.read_json(decoded_response)
            return data_df
        else:
            return decoded_response
    else:
        return 'None'


api_route = '/list_variants'
df_variants = request_to_api(api_route)


def layout():
    return dbc.Row(
        dbc.Col(
            [
                location,
                html.H1('Stage 1 - Variant classification and expert training'),
                html.Br(),

                html.P(children='Please select a variant from database:'),
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
                dbc.Button(children='View details', id='btn-view-variant-details', n_clicks=0, color='primary'),
                html.Br(),
                html.Br(),
                html.Div(
                    id='details-container',
                    children=[
                        html.H2(id='variant-info-title', children='Variant info'),
                        html.Div(id='variant-info-basic'),
                        html.H3('Kaviar'),
                        html.Div(id='variant-info-kaviar'),
                        html.H3('Gwava'),
                        html.Div(id='variant-info-gwava'),
                    ],
                    style={'display': 'none'},
                ),
            ], width=12)
    )
    # if current_user.is_authenticated:


global n_clicks_view_variant
n_clicks_view_variant = 0


@app.callback(
    [
        Output('variant-info-title', 'children'),
        Output('variant-info-basic', 'children'),
        Output('variant-info-kaviar', 'children'),
        Output('variant-info-gwava', 'children'),
        Output('details-container', 'style')
    ],
    [
        Input('datatable-interactivity', 'selected_rows'),
        Input('btn-view-variant-details', 'n_clicks')
    ]
)
def view_variant(sel_rows, n_clicks):
    """
    Load and display information of selected variant
    :param sel_rows: selected rows indices
    :param n_clicks: n clicks in the 'show info' button
    :return: [title, table, table, table, style]
    """
    global n_clicks_view_variant
    if sel_rows is not None and n_clicks_view_variant != n_clicks:
        n_clicks_view_variant = n_clicks
        if len(sel_rows) == 1:  # avoid errors when no row is selected
            # get variant id from initially loaded dataframe
            selected_variant_id = df_variants.at[sel_rows[0], 'ID']
            print('selected_variant is:', selected_variant_id)

            # request variant data to API
            route = '/get_variant'
            data = {'variant_id': int(selected_variant_id)}
            df_selected_variant = request_to_api(route, data, True)

            title = 'Info of variant ' + str(selected_variant_id)

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

    return ['', '', '', '', {'display': 'none'}]
