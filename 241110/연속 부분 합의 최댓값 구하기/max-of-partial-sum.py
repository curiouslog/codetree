# 입력 받기
n = int(input())  # 원소의 개수
arr = list(map(int, input().split()))  # 수열 입력

# 카데인 알고리즘을 위한 변수 초기화
max_sum = arr[0]  # 첫 번째 원소로 초기화 (최대값)
current_sum = arr[0]  # 현재까지의 부분합

# 수열의 두 번째 원소부터 끝까지 순차적으로 처리
for i in range(1, n):
    # 현재 원소를 포함한 부분 수열의 합을 계산
    current_sum = max(arr[i], current_sum + arr[i])
    # 최대 부분합을 갱신
    max_sum = max(max_sum, current_sum)

# 결과 출력
print(max_sum)