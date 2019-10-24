#!/usr/bin/env python3

import sqlite3
# from flask import g
import os

DATABASE = "db/data.db"


def recreate_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("DROP TABLE messages")
    cur.execute("CREATE TABLE messages (header TEXT, body TEXT, author TEXT);")
    conn.commit()
    cur.execute("INSERT INTO messages VALUES('Breaking news!', 'In Python, everything is done by reference. It doesn’t support pointers.', 'Andreas');")
    cur.execute("INSERT INTO messages VALUES('Danske nyheder', 'Jorden er rund ... vi troede altid, at den var flad.', 'Emil');")
    cur.execute("INSERT INTO messages VALUES('WANTED!', 'Someone else that likes php...', 'Mikael');")
    conn.commit()
    conn.close()

def add_to_database(data):
    """
    Function for adding data to database
    """
    new_header = data.get("header")
    new_body = data.get("body")
    new_author = data.get("author")

    sql = "INSERT INTO messages (header, body, author) VALUES ('{}', '{}', '{}');".format(new_header, new_body, new_author)

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def get_all_from_database():
    """
    Function for getting all data from database
    """
    cur = sqlite3.connect(DATABASE).cursor()
    return cur.execute("SELECT * FROM messages")
