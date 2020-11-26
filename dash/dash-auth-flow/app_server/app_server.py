#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main script of the server, used to publish all the routes of the API
"""

from flask import Flask, render_template, request

import config
import database as db

server = Flask(__name__)


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


@server.route('/set_user_classification', methods=['POST'])
def post():
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


@server.route('/list_non_conflictive_variants', methods=['GET'])
def list_non_conflictive_variants():
    """
    List all the non-conflictive variants in the database
    :return: response (JSON)
    """
    status, data = db.list_non_conflictive_variants()
    return generate_json_response(status, data)


@server.route('/list_conflictive_variants', methods=['GET'])
def list_conflictive_variants():
    """
    List all the conflictive variants in the database
    :return: response (JSON)
    """
    status, data = db.list_conflictive_variants()
    return generate_json_response(status, data)


@server.route('/list_labels', methods=['GET'])
def list_labels():
    """
    List all the labels in the database
    :return: response (JSON)
    """
    status, data = db.list_labels()
    return generate_json_response(status, data)


@server.route('/list_levels', methods=['GET'])
def list_levels():
    """
    List all the expertise levels in the database
    :return: response (JSON)
    """
    status, data = db.list_levels()
    return generate_json_response(status, data)


@server.route('/get_variant', methods=['POST'])
def get_variant():
    """
    Get all the attributes of a specific or a random variant
    :return: response (JSON)
    """
    error = False
    if 'variant_id' in request.form:
        variant_id = request.form['variant_id']
        if represents_int(variant_id):
            variant_id = int(variant_id)
            if variant_id == -1:
                # random variant
                print('> Requested a random variant')
                status, data = db.get_random_variant()
            elif variant_id > 0:
                # specific variant
                print('> Requested variant:', variant_id)
                status, data = db.get_variant(variant_id)
            else:
                error = True
        else:
            error = True
    else:
        error = True

    if error:
        status = 'error'
        data = 'RequestError'

    return generate_json_response(status, data)


if __name__ == "__main__":
    server.run(debug=True, host=config.server_ip, port=config.server_port)
