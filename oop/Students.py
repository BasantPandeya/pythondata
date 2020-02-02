# class Students:
#     name='admin'
#
#     def get_name(self):
#         print(self.name)
#
#
# obj1=Students()
# obj1.get_name()

# class Students:
#
#     def __init__(self):
#         print("hello class")
#
# obj1 = Students()

# class Students:
#
#     def __init__(self,name):
#         print(f"hello {name} k xa tero halli challi, sikekai xas hai programming")
#
# obj1 = Students('basant')

class Students:
    name=''

    def __init__(self,name):
        self.name=name

    def get_name(self):
        print(f'your name is {self.name}')

obj1 = Students('basant')
obj1.get_name()

