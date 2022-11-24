def Decor(func):
    global sm
    sm = 0
    def Inner():
        global sm
        func()
        sm += 1
        print(f"Count : {sm}")
    return Inner

@Decor
def test():
    x = 1
    print(x)

test()
test()
test()
test()
test()