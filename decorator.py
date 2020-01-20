def get_doc(anyfunctionhere):
    def innherfunction():
        return anyfunctionhere.__doc__

    return innherfunction

@get_doc
def getname(name):
    """i am user's name"""
    return "all name"

print(getname())
