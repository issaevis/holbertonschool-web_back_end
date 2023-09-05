#!/usr/bin/env python3
'''lists all documents in a collection'''

import pymongo


def list_all(mongo_collection):
    '''returns all documents in a collection'''
    results = list()
    for document in mongo_collection.find():
        results.append(document)

    return results
