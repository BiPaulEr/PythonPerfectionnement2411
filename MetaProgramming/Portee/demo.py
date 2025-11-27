def exterieur():
    test = 1
    def interieur():
        global test
        test = 2
        print('interieur:', test)
    interieur()
    print('exterieur:', test)

test = 0 
exterieur()
print('global:', test)