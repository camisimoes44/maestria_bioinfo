#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script is intended to contain all the functions to communicate with database
"""

import MySQLdb
import config


def prueba_select():
    db_conn = MySQLdb.connect(host=config.db_host, user=config.db_user, passwd=config.db_passwd, db=config.db_name,
                              port=config.db_port)
    query = "SELECT * FROM INNODB_SYS_TABLES"
    cursor = db_conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    db_conn.close()
    return data
