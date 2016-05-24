import aeupdates.settings
import pymongo

THE_MONGO_CLIENT = pymongo.MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
