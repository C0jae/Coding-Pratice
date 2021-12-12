# 결과값 및 카운트 변수 선언 및 정의
result = 0
cnt = 0

# 각 변수값 입력받기
n, m, k = map(int, input("입력 : ").split())

# 배열 입력받기
arr = list(map(int, input("배열 입력 : ").split()))

# 입력받은 배열 올림차순 정렬하기 -> 가장큰수 : arr[n-1], 두번재로 큰 수 : arr[n-2]
arr.sort()

# 결과값 구하기
for i in range(m):
    # 같은수를 더할 수 있을때까지 더하면서 카운트 증가    
    if (cnt != k):
        result += arr[n-1]
        cnt += 1
    # k번만큼 반복한 후 두번째로 높은 수를 더한 후 카운트 초기화
    else:
        result += arr[n-2]
        cnt = 0

print(result)
    