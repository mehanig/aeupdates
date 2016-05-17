from aeupdates import gMongoClient
from aeupdates.settings import MONGO_DB
import pymongo


def get_mongo_db(dbname="mongo"):
    if dbname in gMongoClient:
        return gMongoClient[dbname]

    if dbname in MONGO_DB:
        with MONGO_DB[dbname] as config:
            gMongoClient = pymongo.MongoClient(config["HOST"],
                                               config["PORT"])
    else:
        gMongoClient[dbname] = None

    return gMongoClient[dbname]
