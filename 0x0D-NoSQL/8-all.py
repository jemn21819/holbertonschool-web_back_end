#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""
import pprint
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Python function that lists all documents in a collection
    """
    return mongo_collection.find()
