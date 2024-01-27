#!/usr/bin/env python3
""" module with insert_school fn """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection
        mongo_collection: pymongo collection object
        kwargs: dict argument
    """
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
