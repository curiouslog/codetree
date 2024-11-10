# 입력 받기
N, M = map(int, input().split())
coins = list(map(int, input().split()))

# DP 배열 초기화 (M+1 크기, 불가능한 값으로 초기화)
dp = [float('inf')] * (M + 1)
dp[0] = 0  # 0원을 만드는 데 필요한 동전의 수는 0개

# 동전의 종류를 하나씩 처리하면서 DP 배열을 갱신
for coin in coins:
    for i in range(coin, M + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

# 결과 출력
if dp[M] == float('inf'):
    print(-1)
else:
    print(dp[M])