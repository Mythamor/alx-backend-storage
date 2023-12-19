#!/usr/bin/env python3

"""
Module: 102-log_stats.py
"""


from pymongo import MongoClient


def log_stats(collection):
    """
    script that provides some stats about Nginx logs stored in MongoDB
    """

    # Total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Method stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check stats
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Print the top 10 most present IPs
    print("IPS:")

    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
            ]

    top_ips = collection.aggregate(pipeline)

    for ips in top_ips:
        print(f"\t{ips['_id']}: {ips['count']}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    log_stats(collection)
