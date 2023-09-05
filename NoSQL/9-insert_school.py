#!/usr/bin/env python3
'''lists all documents in a collection'''

import pymongo


def insert_school(mongo_collection, **kwargs):
    res = mongo_collection.insert_one(kwargs)

    return res.inserted_id