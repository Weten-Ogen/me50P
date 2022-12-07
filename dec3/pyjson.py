import json

# person = {
#     'name': 'Marcus',
#     'age' : 23,
#     'city': 'Kumasi',
#     'country': 'Ghana',
#     'siblings': ['Young', 'Precious'],
#     'occupation': 'Software eng',
#     'married' : False,
# }
# jsonf = json.dumps(person, indent=4,sort_keys=True)
# print(jsonf)

# person = json.loads(jsonf)
# print(person)

class User :
    def __init__(self,name,age):
        self.name = name
        self.age = age

M = User('Marcus', 23)

def serialize(o):
    if isinstance(o, User):
        return {'name':o.name,'age':o.age,o.__class__.__name__: True}
    else:
        raise TypeError('Object is not serializable')
    



from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name':o.name,'age':o.age,o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)

with open('person.json', 'w') as file:
    json.dump(M,file,cls=UserEncoder, indent=4)