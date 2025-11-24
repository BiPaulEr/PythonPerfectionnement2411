import time 

def decorator(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end =  time.time()
        print(f"{func.__name__} : {end-begin}s")
    return wrapper

@decorator
def function_simple():
    print("Je suis dans la function")
    time.sleep(3)
    print("Je suis dans la function")


@decorator
def function_simple_3(name = "Inconnu", nom = "Inconnu"):
    time.sleep(5)
    print(f"Je suis {name} {nom}")

function_simple()

function_simple_3(nom="Paul")
#TypeError: decorator.<locals>.wrapper() got an unexpected keyword argument 'nom'