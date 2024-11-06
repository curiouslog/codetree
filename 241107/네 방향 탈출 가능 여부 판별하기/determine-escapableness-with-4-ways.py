n, m = map(int, input().split())

# 이차원 배열 입력 받기
mat = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 방문 확인 배열 생성
visited = [
    [False] * m for _ in range(n)
]

# 결과 변수 초기화
result = 0

# BFS 함수 정의
def bfs(x, y):
    global result
    
    # 초기 위치 방문 처리 및 큐 초기화
    queue = [(x, y)]
    visited[x][y] = True

    # 이동 방향 정의 (상, 하, 좌, 우)
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.pop(0)

        # 우측 하단 도착 시 경로가 존재하므로 결과를 1로 설정하고 종료
        if x == n - 1 and y == m - 1:
            result = 1
            return

        # 상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 이동이 가능한 위치인지 확인
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny))  # 큐에 추가

# BFS 호출
bfs(0, 0)

# 결과 출력
print(result)