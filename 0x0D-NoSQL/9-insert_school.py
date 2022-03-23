#!/usr/bin/env python3
"""
inserts a new document in a collection based on kwargs
"""
import pprint
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    document = {}

    for k, v in kwargs.items():
        document[str(k)] = v
    return mongo_collection.insert(document)
