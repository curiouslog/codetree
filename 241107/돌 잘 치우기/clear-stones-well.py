import copy as cp

n, k, m = map(int, input().split())

mat = [
    list(map(int, input().split()))
    for _ in range(n)
]

start = [
    list(map(int, input().split()))
    for _ in range(k)
]

one_idx = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            one_idx.append([i, j])

idx_list = []
idx = []

def choose_idx(c_num, num):
    if c_num == m:
        idx_list.append(idx[:])
        return
    
    for i in range(num, len(one_idx)):
        idx.append(one_idx[i])
        choose_idx(c_num + 1, i + 1)
        idx.pop()

visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    visited[x][y] = True
    queue = [[x, y]]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and new_mat[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx, ny])

def count_visit():
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count += 1
    return count

choose_idx(0, 0)

max_count = 0

for i in idx_list:
    new_mat = cp.deepcopy(mat)
    for xx, yy in i:
        new_mat[xx][yy] = 0
    visited = [[False] * n for _ in range(n)]
    for xxx, yyy in start:
        bfs(xxx - 1, yyy - 1)
    c = count_visit()
    if c > max_count:
        max_count = c

print(max_count)