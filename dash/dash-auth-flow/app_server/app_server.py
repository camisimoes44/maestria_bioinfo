#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import config
import database as db

server = Flask(__name__)


@server.route('/prueba_get', methods=['GET'])
def get():
    return {'estado': 'OK'}


@server.route('/prueba_post', methods=['POST'])
def post():
    if 'x' in request.form:
        x = request.form['x']
    return {'x': x}


@server.route('/listado', methods=['POST'])
def listado():
    # if 'x' in request.form:
    #     x = request.form['x']
    data = db.prueba_select()
    ids = []
    tablas = []
    for d in data:
        ids.append(d[0])
        tablas.append(d[1])
    data_json = {'ids': ids, 'tablas': tablas}
    return data_json


if __name__ == "__main__":
    server.run(host=config.server_ip, port=config.server_port)
