# 입력 받기
N, M = map(int, input().split())  # 보석의 개수 N과 무게 한도 M
jewels = [tuple(map(int, input().split())) for _ in range(N)]  # 각 보석의 무게와 가치

# DP 배열 초기화
dp = [0] * (M + 1)

# DP 계산
for w, v in jewels:
    for i in range(w, M + 1):  # 현재 무게에서 w 이상일 때부터 갱신
        dp[i] = max(dp[i], dp[i - w] + v)

# 결과 출력
print(dp[M])