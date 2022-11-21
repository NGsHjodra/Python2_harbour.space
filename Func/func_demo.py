"""
def demo(x: float):
    return x * 10


some_var = demo
print(some_var(5))
"""

#second order function or clossure
def generate_processor(multiplier:float):

    param = multiplier**2

    def demo_two(x: float, y:float):
        return (x+y+param)*multiplier
    return demo_two

#res = generate_processor(5)
#print(res(4,6))

methods = [generate_processor(i) for i in range(10)]

print(methods[2](6,4))