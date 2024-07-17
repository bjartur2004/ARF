#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query

db = TinyDB("ARFMasterdb.json")
slaves = db.table('slaves')

q = Query()

def insert_renderSlave(name, ip):
    slaves.insert({'name':name, 'ip':ip})

def get_renderSlaves():
    return slaves.all()