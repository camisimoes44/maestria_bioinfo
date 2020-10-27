#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script is intended to contain all the functions to communicate with MySQL database
"""

import MySQLdb
import config
import simplejson


def mysql_execute_query(query):
    """
    Execute a MySQL query over the configured connection
    :param query: MySQL query to execute
    :return: query result (JSON)
    """
    db_conn = MySQLdb.connect(host=config.db_host, user=config.db_user, passwd=config.db_passwd, db=config.db_name,
                              port=config.db_port)
    cursor = db_conn.cursor()
    cursor.execute(query)
    db_conn.close()
    data_json = mysql_result_to_json(cursor)
    return data_json


def mysql_result_to_json(cursor):
    """
    Convert a MySQL result into JSON.
    Use SimpleJSON to handle Decimal values.
    :param cursor: MySQL cursor
    :return: query result (JSON)
    """
    data = cursor.fetchall()
    json_data = []
    row_headers = [x[0] for x in cursor.description]  # this will extract row headers
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    return simplejson.dumps(json_data)  # use simplejson to handle Decimal values


def list_variants():
    """
    List some attributes of all the variants in database
    :return: query result (JSON)
    """
    query = "SELECT ID, Chr, Start, End, Ref, Alt, `Func.refGene`, `Gene.refGene` FROM variants"
    return mysql_execute_query(query)


def get_variant(id):
    """
    Get the data of a variant form database
    :param id: ID of variant (integer)
    :return: query result (JSON)
    """
    query = "SELECT * FROM variants WHERE ID=" + str(id)
    return mysql_execute_query(query)
