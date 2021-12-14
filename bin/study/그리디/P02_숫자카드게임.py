#n, m값 입력
n, m = map(int, input("n, m값 입력 : ").split())

# 결과값 변수 선언 및 정의
result = 0

# 배열 생성후 최소값 산출 및 result와 비교하여 최대값 산출 및 정의 -> n번만큼 반복
for i in range(n):
    arr = list(map(int, input("카드값 입력 : ").split()))
    min_value = min(arr)
    
    if (min_value >= result):
        result = min_value

print(result)