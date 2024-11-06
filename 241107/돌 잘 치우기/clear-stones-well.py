n, k, m = map(int, input().split())

mat = [
    list(map(int, input().split()))
    for _ in range(n)
]

start = [
    list(map(int, input().split()))
    for _ in range(k)
]

count = 0

for i in range(n):
    for j in range(n):
        if mat[i][j] == 0:
            count += 1

count += m

print(count)