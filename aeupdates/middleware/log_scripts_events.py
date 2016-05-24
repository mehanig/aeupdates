import base64
import json
from apps.products.models import Product
from aeupdates.utils.mongo_tools import get_mongo_db


def is_scripts_api_path(path):
    all_products = Product.objects.all()
    for product in all_products:
        if product.url.split('/')[1:] ==(path.split('/')[1:]):
            return True
    return False


# TODO: Implement logging to mongodb
def log_to_db(data):
    db = get_mongo_db()
    db.all_stats.insert_one(data)


# TODO: decode object from base64 encoded key
def decode_key_data(key):
    key = base64.b64decode(key, validate=False).decode('utf-8')
    key = json.loads(key)
    return key


class ScriptsRequestsLoggerMiddleware(object):
    def process_request(self, request):
        path = request.path
        if is_scripts_api_path(path):
            key = request.META.get('HTTP_AEUPDATESDATA')
            if key:
                data = decode_key_data(key)
                log_to_db(data)
        return None
