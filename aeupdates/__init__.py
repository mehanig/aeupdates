from django.conf import settings
import pymongo

THE_MONGO_CLIENT = pymongo.MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
