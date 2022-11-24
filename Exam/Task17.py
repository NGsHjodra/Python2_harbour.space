class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    # can be another name than self    
    def __add__(self, other):
        Prod_x = self.x + other.x
        Prod_y = self.y + other.y
        return Point(Prod_x, Prod_y)
        
P_a = Point(5,4)
P_x = Point(3,1)
P_b = P_a+P_x

print(type(P_b))
print(P_b.x)
print(P_b.y)