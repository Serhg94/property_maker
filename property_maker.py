def make_func_get(name):
    def func_get(self):
        return getattr(self, "%s" % name)
    return func_get

def make_func_set(name):
    def func_set(self, value):
        setattr(self, "" + name, value)
    return func_set


class property_maker(type):

    base_attrs = dir(type('dummy', (object,), {}))

    def new(cls, clsname, bases, attrs):
        result_attrs = {}
        for name, value in attrs.items():
            if not name.startswith("_") and not property_maker.base_attrs.count(name) and not callable(value):
                result_attrs["" + name] = value
                result_attrs[name] = property(make_func_get(name), make_func_set(name))
            else:
                result_attrs[name] = value
        instance = super(property_maker, cls).__new(cls, clsname, bases, result_attrs)
        return instance