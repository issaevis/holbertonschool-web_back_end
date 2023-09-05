#!/usr/bin/env python3
'''prints stats for a nginx log file'''
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})
if total_logs != 0:
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in http_methods}

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
else:
    print('''
0 logs
Methods:
\tmethod GET: 0
\tmethod POST: 0
\tmethod PUT: 0
\tmethod PATCH: 0
\tmethod DELETE: 0
0 status check

''')
client.close()
