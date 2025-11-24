def decorator(func):
    def wrapper():
        print("Je suis dans le decorator")
        func()
        print("Je suis dans le decorator")
    return wrapper

def function_simple():
    print("Je suis dans la function")

fonction_decorer = decorator(function_simple)

fonction_decorer()