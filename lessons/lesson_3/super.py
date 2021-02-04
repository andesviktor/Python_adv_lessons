class Base:
    def __init__(self):
        print('Base class created')

    def func(self):
        print('This is func from BASE')

class Child(Base):
    def __init__(self):
        # super().__init__()
        Base.__init__(self)
        print('Child class created')

    def func(self):
        super().func()
        print('This is func from CHILD')
c = Child()
print(dir(c))