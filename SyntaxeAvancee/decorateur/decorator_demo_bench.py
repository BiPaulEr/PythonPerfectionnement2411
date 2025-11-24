import time 

def decorator_bench(func):
    def wrapper():
        begin = time.time()
        func()
        end =  time.time()
        print(f"{func.__name__} : {end-begin}s")
    return wrapper

@decorator_bench
def function_simple():
    print("Je suis dans la function")
    time.sleep(3)
    print("Je suis dans la function")
#function_simple = decorator_bench(function_simple)

def function_simple_2():
    print("Je suis dans la function2")
    time.sleep(5)
    print("Je suis dans la function2")
function_simple2 = decorator_bench(function_simple)

function_simple()
function_simple_2()