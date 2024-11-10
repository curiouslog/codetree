n, h, m = map(int, input().split())

mat = [
    list(map(int, input().split()))
    for _ in range(n)
]

first_location = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            first_location.append([i, j, -1])


def bfs(location):
    visited = [[-1] * n for _ in range(n)]
    a, b, c = location
    visited[a][b] = 0
    queue = [[a, b]]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    while queue:
        x, y = queue.pop(0)
        if mat[x][y] == 3:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and visited[nx][ny] == -1 and mat[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    if mat[x][y] == 3:
        return visited[x][y]
    else:
        return -1

for i in range(len(first_location)):
    first_location[i][2] = bfs(first_location[i])

output = [
    [0] * n for _ in range(n)
]

for loc in first_location:
    x, y, count = loc
    output[x][y] = count

for i in range(n):
    for j in range(n):
        print(output[i][j], end=" ")
    print()