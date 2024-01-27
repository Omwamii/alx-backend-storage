#!/usr/bin/env python3
""" module with list_all fn """


def list_all(mongo_collection):
    """ lists all documents in a collection
        mongo_collection: pymongo collection object
    """
    return mongo_collection.find()
