x = [1, 2, 3]
print(super(list, x).__repr__()) 
y = x
print(super(list, y).__repr__())

import copy

z = copy.deepcopy(x)
print(super(list, z).__repr__())

def func(x):
    x[1] = 42

func(copy.deepcopy(x))

print(x) #"[1, 42, 3]"