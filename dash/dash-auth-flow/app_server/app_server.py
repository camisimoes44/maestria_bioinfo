#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main script of the server, used to publish all the routes of the API
"""

from flask import Flask, render_template, request
from passlib.hash import sha256_crypt
import json

import config
import database as db

server = Flask(__name__)

api_v1_base = '/api/v1'

def generate_json_response(status, data):
    """
    Generate a JSON response to be returned by the services
    :param status: status of the response, i.e.: ok, error
    :param data: data of the response, i.e.: JSON, error type, etc
    :return: response (JSON)
    """
    return {"status": status, "data": data}


def represents_int(value):
    """
    Check if the value represents an integer
    :param value: value to check
    :return: boolean
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


@server.route(api_v1_base + '/users/classifications/set', methods=['POST'])
def set_classification():
    """
    Save a classification of a variant
    :return: response (JSON)
    """
    if 'user_id' in request.form and 'variant_id' in request.form and \
            'label_id' in request.form and 'is_correct' in request.form:
        variant_id = request.form['variant_id']
        user_id = request.form['user_id']
        label_id = request.form['label_id']
        is_correct = request.form['is_correct']
        status, data = db.set_user_classification(user_id, variant_id, label_id, is_correct)
        # print(user_id, variant_id, label_id, is_correct)
        if status == 'ok':
            # classification was inserted
            data = 'The classification was saved!'
    else:
        status = 'error'
        data = 'RequestError'

    return generate_json_response(status, data)


@server.route(api_v1_base + '/variants/nonconf', methods=['GET'])
def list_non_conflictive_variants():
    """
    List all the non-conflictive variants in the database
    :return: response (JSON)
    """
    status, data = db.list_non_conflictive_variants()
    return generate_json_response(status, data)


@server.route(api_v1_base + '/variants/conf', methods=['GET'])
def list_conflictive_variants():
    """
    List all the conflictive variants in the database
    :return: response (JSON)
    """
    status, data = db.list_conflictive_variants()
    return generate_json_response(status, data)


@server.route(api_v1_base + '/labels', methods=['GET'])
def list_labels():
    """
    List all the labels in the database
    :return: response (JSON)
    """
    status, data = db.list_labels()
    return generate_json_response(status, data)


@server.route(api_v1_base + '/levels', methods=['GET'])
def list_levels():
    """
    List all the expertise levels in the database
    :return: response (JSON)
    """
    status, data = db.list_levels()
    return generate_json_response(status, data)


@server.route(api_v1_base + '/variants/<int:variant_id>', methods=['GET'])
def get_variant(variant_id):
    """
    Get all the attributes of a specific or a random variant
    :param: variant_id
    :return: response (JSON)
    """
    error = False
    # check if the received ID is an integer, otherwise return an error
    if represents_int(variant_id):
        variant_id = int(variant_id)
        if variant_id > 0:
            # specific variant
            print('> Requested variant:', variant_id)
            status, data = db.get_variant(variant_id)
        else:
            error = True
    else:
        error = True

    if error:
        status = 'error'
        data = 'RequestError'

    return generate_json_response(status, data)


@server.route(api_v1_base + '/variants/nonconf/random', methods=['GET'])
def get_nonconf_random_variant():
    """
    Get all the attributes of a random variant
    :return: response (JSON)
    """
    print('> Requested a random variant')
    status, data = db.get_random_variant()

    return generate_json_response(status, data)


@server.route(api_v1_base + '/users/login', methods=['POST'])
def login():
    """
    Validate user and password to login
    :return: response (JSON)
    """
    if 'user' in request.form and 'password' in request.form:
        user = request.form['user']
        user_password = request.form['password']

        # print(sha256_crypt.hash(user_password))
        # password2 = sha256_crypt.hash("password")

        # print(password)
        # print(password2)
        # print(sha256_crypt.verify(password, password2))

        status, data = db.get_user_data(user)
        if data is None or data == '[]':
            # user does not exist
            print('>>> LoginError:', user, '. Wrong user.')
            status = 'error'
            data = 'LoginError'
        else:
            json_user_data = json.loads(data)[0]
            hashed_password_db = json_user_data['password']
            if sha256_crypt.verify(user_password, hashed_password_db):
                # password OK
                print('>>> LoginOK:', user)
                del json_user_data['password']  # delete the hashed password from the response
                status = 'ok'
                data = json_user_data
            else:
                # wrong password
                print('>>> LoginError:', user, '. Wrong password.')
                status = 'error'
                data = 'LoginError'
    else:
        status = 'error'
        data = 'RequestError'

    return generate_json_response(status, data)


if __name__ == "__main__":
    server.run(debug=True, host=config.server_ip, port=config.server_port)
