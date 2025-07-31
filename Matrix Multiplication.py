x, y, z = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(x)]

B = [list(map(int, input().split())) for _ in range(y)]

C = [[0] * z for _ in range(x)]

for i in range(x):
    for j in range(z):          
        for k in range(y):      
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(*row)
