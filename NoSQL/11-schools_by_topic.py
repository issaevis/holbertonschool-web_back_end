#!/usr/bin/env python3
'''lists all documents in a collection'''

import pymongo


def schools_by_topic(mongo_collection, topic):
    '''returns a list of all documents that have a specific topic'''
    schools = mongo_collection.find({"topics": topic})
    school_list = list(schools)
    return school_list
