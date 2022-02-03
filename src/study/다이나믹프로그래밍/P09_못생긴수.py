n = int(input("n번째 못생긴 수 검색 : "))

# n번째 수까지 나타낼 수 있는 data 리스트 생성
data = [0] * (n + 1)

# 인덱스 1번(1첫째 수) = 1로 지정
data[1] = 1

# 2배, 3배, 5배를 위한 인덱스 선언
i2 = i3 = i5 = 1

# 처음 곱셈 값 초기화
multiply_2, multiply_3, multiply_5 = 2, 3, 5

# 2번째부터 n번째까지의 못생긴 수 구하기
for i in range(2, n + 1):
    # 낮은수부터 적용되므로 곱셈값들중 최소값을 i번째로 지정
    data[i] = min(multiply_2, multiply_3, multiply_5)
    
    if data[i] == multiply_2:
        # 인덱스 1 추가
        i2 += 1
        # 다음 곱셈값으로 적용
        multiply_2 = data[i2] * 2
    
    if data[i] == multiply_3:
        i3 += 1
        multiply_3 = data[i3] * 3
        
    if data[i] == multiply_5:
        i5 += 1
        multiply_5 = data[i5] * 5

# n번째 못생긴 수 출력
print(data[n])


n = int(input())

data = [0] * (n + 1)

data[1] = 1

i2 = i3 = i5 = 1
mul_2, mul_3, mul_5 = 2, 3, 5

for i in range(2, n + 1):
    data[i] = min(mul_2, mul_3, mul_5)
    
    if data[i] == mul_2:
        i2 += 1
        mul_2 = data[i2] * 2
        
    if data[i] == mul_3:
        i3 += 1
        mul_3 = data[i3] * 3
        
    if data[i] == mul_5:
        i5 += 1
        mul_5 = data[i5] * 5
        
print(data[n])