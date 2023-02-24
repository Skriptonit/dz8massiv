n, m = [int(x) for x in input().split()]
a = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            a[i][j] = "*"

for s in a:
    print(*s)
