# 입력 처리
n = int(input())  # 층 수
treasure = [tuple(map(int, input().split())) for _ in range(n)]  # 각 층의 보물 개수 (l, m, r)

# DP 배열 초기화
dp = [[0] * 3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = treasure[0]  # 1층의 보물 개수로 초기화

# DP 진행
for i in range(1, n):
    l, m, r = treasure[i]
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + l  # 왼쪽 방
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + m  # 가운데 방
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + r  # 오른쪽 방

# 마지막 층의 예외 처리
# 1층에서 들어간 방과 다른 방들 중 최대값 선택
max_treasure = 0
for j in range(3):
    for k in range(3):
        if j != k:
            max_treasure = max(max_treasure, dp[n-1][k])

# 결과 출력
print(max_treasure)