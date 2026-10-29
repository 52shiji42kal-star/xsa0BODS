# matrix2
M = 4
N = 3
matrix = []
for i in range(M):
    row = []
    for j in range(1, N + 1):
        row.append(5 * j)
    matrix.append(row)
print(matrix)

# matrix3
M = 3
N = 4
numbers = [10, 20, 30]
matrix = []
for i in range(M):
    row = [numbers[i]] * N
    matrix.append(row)
print(matrix)

# matrix5
M = 3
N = 4
D = 5
numbers = [1, 2, 3]
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(numbers[i] + j * D)
    matrix.append(row)
print(matrix)

# matrix6
M = 4
N = 3
Q = 2
numbers = [1, 3, 5]
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(numbers[j] * (Q ** i))
    matrix.append(row)
print(matrix)

# matrix10
matrix = [,
 ,
    [9, 10, 11, 12]
]
M = len(matrix)
N = len(matrix[0])
for j in range(0, N, 2):
    for i in range(M):
        print(matrix[i][j])
