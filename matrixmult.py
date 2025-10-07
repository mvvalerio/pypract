# "matrixmult.py" Is a simple program which takes two 2D matrices and returns
# their product

matrix1 = [[6, 7],
            [12, 14]]

matrix2 = [[9, 15],
            [18, 30]]

result = [[0, 0],
           [0, 0]]

for x in range(2):
    for z in range(2):
        result[x][z] = (matrix1[x][0] * matrix2[0][z] + 
                        matrix1[x][1] * matrix2[1][z])

for row in result:
    print(row)
