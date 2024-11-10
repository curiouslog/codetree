# 입력 처리
N, M = map(int, input().split())
sequence = list(map(int, input().split()))

# DP 배열 초기화
# dp[i][j][k]: i번째 숫자까지 고려했을 때, j번 다른 횟수로 k숫자가 마지막일 때 최대 유사도
dp = [[[0] * 5 for _ in range(M + 1)] for _ in range(N)]

# 첫 번째 위치 초기화
for k in range(1, 5):
    dp[0][0 if k == sequence[0] else 1][k] = 1 if k == sequence[0] else 0

# DP 진행
for i in range(1, N):
    for j in range(M + 1):
        for prev in range(1, 5):
            for k in range(1, 5):
                if prev == k:  # 이전 숫자와 같으면 변경 횟수 증가 없음
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][prev] + (1 if k == sequence[i] else 0))
                elif j + 1 <= M:  # 다른 숫자로 변경할 때
                    dp[i][j+1][k] = max(dp[i][j+1][k], dp[i-1][j][prev] + (1 if k == sequence[i] else 0))

# 최대 유사도 계산
max_similarity = 0
for j in range(M + 1):
    for k in range(1, 5):
        max_similarity = max(max_similarity, dp[N-1][j][k])

# 결과 출력
print(max_similarity)