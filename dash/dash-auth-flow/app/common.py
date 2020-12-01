import pandas as pd
import requests
import json
import config


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
