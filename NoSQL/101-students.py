#!/usr/bin/env python3
'''function that returns all students sorted by average score'''


import pymongo


def top_students(mongo_collection):
    '''returns a list with the fields needed by the main'''
    pipeline = [
        {"$unwind": "$topics"},
        {
            "$group": {
                "_id": "$name",
                "averageScore": {"$avg": "$topics.score"},
                "originalDoc": {"$first": "$$ROOT"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]

    results = mongo_collection.aggregate(pipeline)

    # Format the results to include the _id
    formatted_results = []
    for result in results:
        formatted_results.append({
            "_id": result["originalDoc"]["_id"],
            "name": result["_id"],
            "averageScore": result["averageScore"]
        })

    return formatted_results
