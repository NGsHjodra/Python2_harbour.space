def FuncOfFunc(a:float):
    def Product(x:float):
        return a*x
    return Product

Func_a = FuncOfFunc(8)
Prod_a_x = Func_a(10)
print(Prod_a_x)
