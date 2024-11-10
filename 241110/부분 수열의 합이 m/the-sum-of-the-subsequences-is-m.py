# 입력 받기
n, m = map(int, input().split())  # 수열의 크기 n과 목표 합 m
A = list(map(int, input().split()))  # 수열 A의 원소들

# dp 배열을 초기화, dp[i]는 합이 i인 부분 수열의 최소 길이
# m+1 크기로 초기화, 시작할 때 합이 0인 부분 수열은 길이가 0
dp = [float('inf')] * (m + 1)
dp[0] = 0  # 합이 0인 부분 수열은 길이가 0

# 부분 수열 계산
for num in A:
    for i in range(m, num - 1, -1):
        dp[i] = min(dp[i], dp[i - num] + 1)

# dp[m]이 여전히 inf라면, m을 만들 수 없다는 뜻
if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])