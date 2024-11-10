MOD = 1000000007

# n 입력 받기
n = int(input())

# dp 배열 초기화
dp = [0] * (n + 1)

# 초기 조건 설정
dp[0] = 1
if n >= 1:
    dp[1] = 2
if n >= 2:
    dp[2] = 7

# dp 점화식을 사용하여 값 계산
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 5 + dp[i - 3] * 4) % MOD

# 결과 출력
print(dp[n])