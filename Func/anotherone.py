class CachedFactorial:
    def __init__(self) -> None:
        self.cache = {}

    def __calc_factorial(self, n:int) -> int:
        if n <= 1:
            return 1
        return n * self.__calc_factorial(n - 1)

    def __call__(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = self.__calc_factorial(n)
        else:
            print(f"Cache hit for {n}")
        return self.cache[n]

f = CachedFactorial()
res = f(5)
res = f(7)
res = f(9)
res = f(5)
print(res)

class SuperCollection:
    def __iter__(self):
        self.num = 0
        self.index = 0
        return self
    
    def __next__(self):
        if(self.index >= 10):
            raise StopIteration
        self.num += self.index ** 2
        self.index += 1
        return self.num
    
coll = SuperCollection()

for var in coll:
    print(var)