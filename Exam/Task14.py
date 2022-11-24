def Decor(func):
    def Inner():
        print(func.__name__)
        func()
    return Inner

@Decor
def test():
    x = 1
    print(x)

test()