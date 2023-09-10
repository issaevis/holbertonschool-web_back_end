#!/usr/bin/env python3
'''prints stats for a nginx log file'''
from pymongo import MongoClient


def count(elements):
    """Count documents inside a collection"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    return collection.count_documents(elements)


def countv2():
    '''counts the IP's'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]
    result = list(collection.aggregate(pipeline))
    return result


def main():
    """Main function"""
    print(f"{count({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {count({'method': 'GET'})}")
    print(f"\tmethod POST: {count({'method': 'POST'})}")
    print(f"\tmethod PUT: {count({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {count({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {count({'method': 'DELETE'})}")
    print(f"{count({'method': 'GET', 'path': '/status'})} status check")

    print("IPs:")
    result = countv2()
    for doc in result:
        print(f"\t{doc['_id']}: {doc['count']}")


if __name__ == "__main__":
    main()
