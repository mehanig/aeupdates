from django.conf import settings
from aeupdates import THE_MONGO_CLIENT


def get_mongo_db(db_name=settings.MONGO_DB_NAME):
    return THE_MONGO_CLIENT[db_name]
