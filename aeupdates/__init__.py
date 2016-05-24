import aeupdates.settings
import pymongo

THE_MONGO_CLIENT = pymongo.MongoClient(settings.MONGO_HOST, 27017)

def get_mongo_db(db_name):
    return THE_MONGO_CLIENT[db_name]
