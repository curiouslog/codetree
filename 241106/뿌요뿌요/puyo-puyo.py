n = int(input())

explode_block = 0
max_size = 0

mat = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * n for _ in range(n)
]

def dfs(x, y):
    global count

    visited[x][y] = True
    count += 1

    for xx in [xxx + x for xxx in [-1, 1]]:
        if xx >= 0 and xx < n and visited[xx][y] == False and mat[x][y] == mat[xx][y]:
            dfs(xx, y)
    
    for yy in [yyy + y for yyy in [-1, 1]]:
        if yy >= 0 and yy < n and visited[x][yy] == False and mat[x][y] == mat[x][yy]:
            dfs(x, yy)

    return

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            count = 0
            dfs(i, j)
            if count > max_size:
                max_size = count
            if count >= 4:
                explode_block += 1

print(f"{explode_block} {max_size}")