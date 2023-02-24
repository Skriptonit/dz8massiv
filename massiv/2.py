n = int(input())
a = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            a[i][j] = "*"
        elif i == j:
            a[i][j] = "*"
        elif i + j == n - 1:
            a[i][j] = "*"

for s in a:
    print(*s)