def function(limit):
    for num in range(limit, -1, -1):
        print("inside")
        yield num
        print("inside2")

for num in function(5):
    print(num)
for num in function(5):
    print(num)