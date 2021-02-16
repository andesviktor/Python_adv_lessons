import pickle

class User():
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

user = User('Ivan',30)

b_user = pickle.dumps(user)

print(b_user)
print(pickle.loads(b_user).get_name())