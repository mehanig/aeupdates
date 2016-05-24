from aeupdates.settings import MONGO_DB_NAME
from aeupdates import THE_MONGO_CLIENT


def get_mongo_db(db_name=MONGO_DB_NAME):
    return THE_MONGO_CLIENT[db_name]
