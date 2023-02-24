n,m = [int(i) for i in input().split()]

a = [[int(j) for j in input().split()] for i in range(n)]
best_i= 0
best_j= 0
curr_max = -10000000000
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i=i
            best_j=j
print(best_i, best_j)