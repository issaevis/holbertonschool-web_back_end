#!/usr/bin/env python3
'''lists all documents in a collection'''

import pymongo


def update_topics(mongo_collection, name, topics):
    '''updates a document'''

    result = mongo_collection.update_one(
            {"name": name},
            {"$set": {"topics": topics}}
        )
