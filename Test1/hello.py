class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is unappropriated name")

print("Hello my friend")