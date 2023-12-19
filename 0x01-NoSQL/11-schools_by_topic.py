#!/usr/bin/env python3

"""
Module: 11-schools_by_topic.py
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic:
    """
    query = {"topics": topic}
    return mongo_collection.find(query)
