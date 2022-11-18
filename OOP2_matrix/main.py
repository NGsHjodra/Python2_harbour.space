class Matrix2d():
    def __init__(self, listx) -> None:
        self.matrix = [[i for i in lst] for lst in listx]

    def __add__(self, other):
        prod_mat = [[0 for _ in range(2)],[0 for _ in range(2)]]
        for i in range(2):
            for j in range(2):
                prod_mat[i][j] += self.matrix[i][j]+other.matrix[i][j]
        return prod_mat

    def __mul__(self, other):
        prod_mat = [[0 for _ in range(2)],[0 for _ in range(2)]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    prod_mat[i][j] += self.matrix[i][k]*other.matrix[k][j]
        return prod_mat
        

# matrix mul is like all x multiply all y in another mat

a = Matrix2d([[1,2],[3,4]])
b = Matrix2d([[1,3],[5,7]])

c = a*b
d = a+b
print(c)
print(d)