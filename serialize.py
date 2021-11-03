from pprint import pprint
import types

user = {
    "__type__": "User",
    "a": {
        "__type__": "Address",
        "p1": "value1",
        "p2": "value2"
    },
    "b": {
        "__type__": "Policy",
        "p1": {
            "__type__": "Condition",
            "p1": "value1",
            "p2": "value2"
        },
        "p2": "value2"
    },
    "c": "valuec",
    "d": "valued"
}


def __constructor(self, **kwargs):
    for key, value in kwargs:
        setattr(self, key, value)


def __set_attribute(self, name, value):
    self.name = value


def deserialize(jsondoc, constructor=None, set_attribute=None):
    if constructor is None or set_attribute is None:
        raise Exception("Invalid constructor and setattr method provided.")

    __init__config = {
        "__init__": constructor,
        "__setattr__": set_attribute
    }

    main_object = type(jsondoc["__type__"],
                       (object, ), __init__config)
    for key, value in jsondoc.items():
        if type(value) != dict:
            setattr(main_object, key, value)
        elif key != "__type__" and type(value) == dict:
            nested_object = deserialize(
                value, constructor=constructor, set_attribute=set_attribute)
            setattr(main_object, key, nested_object)
    return main_object


def serialize(o):
    def __is_private(key):
        return key[:2] == "__" and key != "__type__"

    def __is_protected(key):
        return key[0] == "_" and key != "__type__"

    jsondoc = {}
    for key, value in o.__dict__.items():
        if not __is_private(key) and not __is_protected(key):
            try:
                prop = serialize(value)
                jsondoc.update({key: prop})
            except:
                jsondoc.update({key: value})
    return jsondoc


u = deserialize(user, constructor=__constructor, set_attribute=__set_attribute)
print(isinstance(u, object))
print(u)
print(u.a)
print(u.b)

pprint(serialize(u))
