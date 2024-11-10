# 입력 받기
N, M = map(int, input().split())  # 옷의 수 N, 날의 수 M
clothes = []
for _ in range(N):
    s, e, v = map(int, input().split())
    clothes.append((s, e, v))  # (입기 시작할 수 있는 날짜, 입을 수 있는 마지막 날짜, 화려함)

# 각 날짜별 입을 수 있는 옷을 저장하는 리스트
available_clothes = [[] for _ in range(M + 1)]
for i, (s, e, v) in enumerate(clothes):
    for day in range(s, e + 1):
        available_clothes[day].append((i, v))  # 옷 인덱스와 화려함을 저장

# DP 배열 초기화
# dp[day][i]는 day번째 날에 i번째 옷을 입었을 때 얻을 수 있는 최대 만족도
dp = [[-1] * N for _ in range(M + 1)]

# 첫 날 초기화
for i, v in available_clothes[1]:
    dp[1][i] = 0  # 첫 날에는 이전 날이 없으므로 만족도 0으로 시작

# DP 진행
for day in range(2, M + 1):
    for i, v_i in available_clothes[day]:
        for j, v_j in available_clothes[day - 1]:
            if dp[day - 1][j] != -1:  # 이전 날에 j번째 옷을 입은 경우만 고려
                dp[day][i] = max(dp[day][i], dp[day - 1][j] + abs(v_i - v_j))

# 마지막 날 최대 만족도 찾기
max_satisfaction = max(dp[M][i] for i, _ in available_clothes[M])

# 결과 출력
print(max_satisfaction)