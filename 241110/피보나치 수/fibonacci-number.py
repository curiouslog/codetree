# N 입력 받기
N = int(input())

# 피보나치 수를 저장할 배열 초기화
dp = [0] * (N + 1)

# 초기 조건 설정
dp[1] = 1
if N > 1:
    dp[2] = 1

# 반복문을 통해 피보나치 수 계산
for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# 결과 출력
print(dp[N])