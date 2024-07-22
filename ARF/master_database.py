#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query

db = TinyDB("ARFMasterdb.json")
slaves = db.table('slaves')

q = Query()

def insert_innit_renderSlave(uuid):
    slaves.insert({'name':"", 'uuid':uuid})

def get_renderSlaves():
    return slaves.all()

def get_renderSlave(key, val):
    if key == "name":
        return slaves.search(q.name == val)
    elif key == "uuid":
        return slaves.search(q.uuid == val)
