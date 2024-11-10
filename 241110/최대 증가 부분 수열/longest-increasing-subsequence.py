# 입력 받기
N = int(input())  # 수열의 크기
nums = list(map(int, input().split()))  # 수열의 원소들

# dp 배열을 N 크기로 초기화, 각 원소는 최소 1로 초기화
dp = [1] * N

# LIS 계산
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:  # nums[i]가 nums[j]보다 크면 증가 부분 수열
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열에서 최댓값을 출력
print(max(dp))