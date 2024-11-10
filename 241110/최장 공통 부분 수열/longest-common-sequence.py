# 입력
A = input().strip()
B = input().strip()

# 문자열 길이
N = len(A)
M = len(B)

# DP 테이블 초기화 (N+1) x (M+1) 크기
dp = [[0] * (M + 1) for _ in range(N + 1)]

# DP 테이블 채우기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i - 1] == B[j - 1]:  # 현재 문자가 같을 때
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 현재 문자가 다를 때
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 결과 출력
print(dp[N][M])