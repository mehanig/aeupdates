# TODO: Check if real script path
def is_scripts_api_path(path):
    return True


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
