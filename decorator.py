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

# use for checking age to enter disco.
# def age_check(anyfunction):
#     def ack(age):
#         if age>=18 and age<=40:
#             return "Welcome to party"
#         else:
#             return "We are sorry. We cannot allow you to enter"
#     return ack
#
# @age_check
# def getage(age):
#     return age
#
# a=int(input('Enter your age: '))
# print(getage(a))


# def zero_check(anyfunction):
#     def zck(a, b):
#         if a>0 and b>0:
#             return a+b
#         else:
#             return "We are sorry. We cannot calculate."
#     return zck
#
# @zero_check
# def getsum(a, b):
#     return a+b
#
# a=int(input('Enter your 1st num: '))
# b=int(input('Enter your 2nd num: '))
# print(getsum(a, b))


# zero check decorator
# @check user name is string or not
# @display documentation
# functionwrap
# def user(name)
#     """something to write"""


# def name_check(anyfunction):
#     def namechk(name):
#         if (name.isdigit()):
#             return "Given name is not string"
#         else:
#             return "Given name is string"
#     return namechk
#
# @name_check
# def getname(name):
#     return type(name)
#
# a=input('Enter your name: ')
# print(getname(a))

