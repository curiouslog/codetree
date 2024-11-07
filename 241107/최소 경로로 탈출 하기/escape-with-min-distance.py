n, m = map(int, input().split())

mat = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[-1] * m for _ in range(n)]

def bfs():
    visited[0][0] = 0
    queue = [[0, 0]]
    dx, dy = [1, 0, -1, 0], [0, 1, 0 , -1]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m and visited[nx][ny] == -1 and mat[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

bfs()
print(visited[n - 1][m - 1])