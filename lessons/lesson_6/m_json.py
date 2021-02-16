import json, datetime


class User:
    def __init__(self, name):
        self.__name = name
        self.__dob = datetime.date(1990, 12, 12)

    def get_name(self):
        return self.__name


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return {'__date__':str(o)}
        return {f'__{o.__class__.__name__}__': o.__dict__}

def decode_object(o):
    if '__User__' in o:
        temp = User(None)
        temp.__dict__.update(o['__User__'])
        return temp
    elif '__datetime' in o:
        return datetime.date.strftime(o['__date__'],'%Y-%m-%d')


user = User('Ivan')

user_json = json.dumps(user, cls=CustomEncoder)
print(user_json)
