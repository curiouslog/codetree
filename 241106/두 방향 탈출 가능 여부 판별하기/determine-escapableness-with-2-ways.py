n, m = map(int, input().split())

result = 0

mat = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    global result

    visited[y][x] = True

    if x == m - 1 and y == n - 1:
        result = 1
        return
    
    if y != n - 1 and mat[y + 1][x] == 1 and visited[y + 1][x] == False:
        dfs(x, y + 1)

    if x != m - 1 and mat[y][x + 1] == 1 and visited[y][x + 1] == False:
        dfs(x + 1, y)

dfs(0, 0)
print(result)