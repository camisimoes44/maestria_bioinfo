#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main script of the server, used to publish all the routes of the API
"""

from flask import Flask, render_template, request

import config
import database as db

server = Flask(__name__)


# @server.route('/prueba_get', methods=['GET'])
# def get():
#     return {'estado': 'OK'}
#
#
# @server.route('/prueba_post', methods=['POST'])
# def post():
#     x = 'empty'
#     if 'x' in request.form:
#         x = request.form['x']
#     return {'x': x}


@server.route('/list_variants', methods=['POST'])
def list_variants():
        return db.list_variants()


@server.route('/get_variant', methods=['POST'])
def get_variant():
    if 'variant_id' in request.form:
        return db.get_variant(request.form['variant_id'])
    else:
        return {'Data': 'None'}

    # id = []
    # chr = []
    # # print(type(data))
    # # print(data)
    # for d in data:
    #     id.append(d[0])
    #     chr.append(d[4])
    # data_json = {'ID': id, 'Chr': chr}
    # return data_json


if __name__ == "__main__":
    server.run(host=config.server_ip, port=config.server_port)
