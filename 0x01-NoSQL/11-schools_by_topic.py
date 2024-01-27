#!/usr/bin/env python3
""" module with school_by_topic """


def schools_by_topic(mongo_collection, topic):
    """ returns list of school having specific topic """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
