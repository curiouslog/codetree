import heapq

# 입력 받기
N = int(input())  # 행렬 크기
matrix = [list(map(int, input().split())) for _ in range(N)]

# dp 배열을 무한대로 초기화 (최솟값을 구하기 위해)
dp = [[float('inf')] * N for _ in range(N)]
dp[0][0] = matrix[0][0]  # 시작점 초기화

# 우선순위 큐 (힙), (최댓값, x, y) 형태로 넣음
# 첫 번째 원소는 dp값으로, 두 번째와 세 번째는 좌표
pq = [(matrix[0][0], 0, 0)]

# 4방향 (오른쪽, 아래쪽)만 이동
directions = [(0, 1), (1, 0)]

while pq:
    # 우선순위 큐에서 최댓값이 최소인 경로를 꺼냄
    max_value, x, y = heapq.heappop(pq)
    
    # (x, y)에 도달하는 최댓값이 dp 값보다 크면 이미 더 좋은 경로를 찾았으므로 건너뛰기
    if max_value > dp[x][y]:
        continue
    
    # 오른쪽과 아래쪽으로 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < N and 0 <= ny < N:
            # 새로운 경로에서의 최댓값은 현재까지의 최댓값과 새로 이동한 칸의 값 중 큰 값
            new_max = max(max_value, matrix[nx][ny])
            
            # 만약 이 새로운 경로의 최댓값이 기존 경로의 최댓값보다 작으면 업데이트
            if new_max < dp[nx][ny]:
                dp[nx][ny] = new_max
                heapq.heappush(pq, (new_max, nx, ny))

# (N-1, N-1)까지 도달하는 최댓값이 최소가 되는 값이 저장됨
print(dp[N-1][N-1])