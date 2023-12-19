#!/usr/bin/env python3

"""
Module: 101-students.py
"""


from pymongo import MongoClient


def top_students(mongo_collection):
    """
    function that returns all students sorted by average score
    """
    students = mongo_collection.find({})
    for student in students:
        total_score = sum(topic['score'] for topic in student['topics'])
        average_score = total_score / len(student['topics'])
        mongo_collection.update_one({'_id': student['_id']}, 
        {"$set": {"averageScore": average_score}})

    top_students = mongo_collection.find({}, {"_id": 1, "name": 1, 
                    "averageScore": 1}).sort([("averageScore", -1)])
    return top_students

