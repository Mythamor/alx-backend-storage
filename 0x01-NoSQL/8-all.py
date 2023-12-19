#!/usr/bin/env python3

"""
Module: 8-all.py
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    Return an empty list if no document in the collection
    """
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
