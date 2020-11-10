#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script is intended to contain all the functions to communicate with the MySQL database
"""

import MySQLdb
import config
import simplejson


def mysql_execute_query(query):
    """
    Execute a MySQL query with the configured connection
    :param query: MySQL query to execute
    :return: query execution status, query result (JSON)/ row count (int)
    """
    try:
        db_conn = MySQLdb.connect(host=config.db_host, user=config.db_user, passwd=config.db_passwd, db=config.db_name,
                                  port=config.db_port)
    except MySQLdb.OperationalError as e:
        print(e)
        return 'error', 'OperationalError'

    try:
        cursor = db_conn.cursor()
        cursor.execute(query)

        if query.upper().startswith('SELECT'):
            # SELECT queries (must return result as JSON)
            db_conn.close()
            data_json = mysql_result_to_json(cursor)
            data = data_json
        else:
            # other queries (must return affected row count)
            db_conn.commit()
            db_conn.close()
            data = cursor.rowcount
        return 'ok', data

    except MySQLdb.DataError as e:
        print(e)
        return 'error', "DataError"

    except MySQLdb.InternalError as e:
        print(e)
        return 'error', "InternalError"

    except MySQLdb.IntegrityError as e:
        print(e)
        return 'error', "IntegrityError"

    except MySQLdb.OperationalError as e:
        print(e)
        return 'error', "OperationalError"

    except MySQLdb.NotSupportedError as e:
        print(e)
        return 'error', "NotSupportedError"

    except MySQLdb.ProgrammingError as e:
        print(e)
        return 'error', "ProgrammingError"

    except:
        print("UnknownError")
        return 'error', "UnknownError"


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
    List some attributes of all the variants in the database
    :return: query result (JSON)
    """
    query = "SELECT ID, Chr, Start, End, Ref, Alt, `Func.refGene`, `Gene.refGene` FROM variants WHERE " \
            "`InterVar_automated` IS NOT NULL "
    return mysql_execute_query(query)


def list_labels():
    """
    List all labels in the database
    :return: query result (JSON)
    """
    query = "SELECT * FROM labels"
    return mysql_execute_query(query)


def list_levels():
    """
    List all expertise levels in the database
    :return: query result (JSON)
    """
    query = "SELECT * FROM expertise_levels"
    return mysql_execute_query(query)


def get_variant(id):
    """
    Get the data of a variant form the database
    :param id: ID of variant (integer)
    :return: query result (JSON)
    """
    query = "SELECT * FROM variants WHERE ID=" + str(id)
    return mysql_execute_query(query)


def set_user_classification(user_id, variant_id, label_id, is_correct):
    """
    Save to database a classification of a variant, performed by a user
    :param user_id: author of classification
    :param variant_id: variant classified
    :param label_id: label assigned to variant
    :param is_correct: result of classification
    :return:
    """
    query = "INSERT INTO user_classification (user_ID, variant_ID, label_ID, is_correct) VALUES ('" + str(user_id) \
            + "', " + str(variant_id) + ", '" + str(label_id) + "', " + str(is_correct) + ") "
    # print(query)
    return mysql_execute_query(query)
