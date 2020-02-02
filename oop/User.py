class User:
    def __init__(self, name):
        self.__name=name

    def test(self):
        return self.__name

obj=User('Ram is tatti')

print(obj.test())
