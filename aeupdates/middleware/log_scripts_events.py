from apps.products.models import Product

def is_scripts_api_path(path):
    all_products = Product.objects.all()
    for product in all_products:
        if product.url.split('/')[1:] ==(path.split('/')[1:]):
            return True
    return False


# TODO: Implement logging to mongodb
def log_to_db(key):
    pass


# TODO: decode object from base64 encoded key
def decode_key_data(key):
    pass


class ScriptsRequestsLoggerMiddleware(object):
    def process_request(self, request):
        path = request.path
        if is_scripts_api_path(path):
            key = request.META.get('HTTP_AEUPDATESDATA')
            if key:
                key = decode_key_data(key)
                log_to_db(key)
        return None
