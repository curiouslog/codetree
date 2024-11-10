# 입력 받기
N = int(input())  # 행렬 크기
matrix = [list(map(int, input().split())) for _ in range(N)]

# dp 배열 초기화
dp = [[0] * N for _ in range(N)]

# 초기 값 설정
dp[0][0] = matrix[0][0]

# 첫 번째 행과 첫 번째 열은 이전 값에서만 올 수 있음
for i in range(1, N):
    dp[0][i] = dp[0][i-1] + matrix[0][i]  # 첫 번째 행은 왼쪽에서만 올 수 있음
    dp[i][0] = dp[i-1][0] + matrix[i][0]  # 첫 번째 열은 위쪽에서만 올 수 있음

# 나머지 dp 배열을 채워나감
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

# 결과 출력 (N, N 지점까지 가는 최대 합)
print(dp[N-1][N-1])