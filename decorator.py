# def get_doc(anyfunctionhere):
#     def innerfunction():
#         return anyfunctionhere.__doc__
#
#     return innerfunction
#
# @get_doc
# def getname(name):
#     """i am user's name"""
#     return "all name"
#
# print(getname())

def age_check(anyfunction):
    def ack(age):
        if age>=18 and age<=40:
            return "Welcome to party"
        else:
            return "We are sorry. We cannot allow you to enter"
    return ack

@age_check
def getage(age):
    return age

a=int(input('Enter your age: '))
print(getage(a))

# zero check decorator
# @check user name is string or not
# @display documentation
# functionwrap
# def user(name)
#     """something to write"""
