def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    result = []
    for i in range(len(a)):
        rows = []
        for j in range(len(b[0])):
            total = 0 
            for k in range(len(a[0])):
                total = total + a[i][k] * b[k][j]
            rows.append(total)
        result.append(rows)
    return result

A = [[1, 2],
     [2, 4]]

B = [[2, 1],
     [3, 4]]