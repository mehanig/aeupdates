class MongoRouter(object):
    def db_for_read(self, model, **hints):
        return getattr(model._meta, 'using', None)

    def db_for_write(self, model, **hints):
        return getattr(model._meta, 'using', None)

    def allow_relation(self, obj1, obj2, **hints):
        # only allow relations within a single database
        if getattr(obj1._meta, 'using', None) == getattr(obj2._meta, 'using', None):
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == getattr(model._meta, 'using', 'default'):
            return True
        return None
