#!/usr/bin/env python3

"""
Module: 10-update_topics.py
"""


def update_topics(mongo_collection, name, topics):
    """
    function that changes all topics of a school document based on the name
    """
    query = {"name": name}
    updated_data = {"$set": {"topics": topics}}
    mongo_collection.update_one(query, updated_data)
