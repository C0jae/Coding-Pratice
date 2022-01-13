n = int(input("삼각형 크기 입력 : "))

# 삼감형 정수가 들어갈 리스트 선언
data = []

for i in range(n):
    data.append(list(map(int, input("정수 입력 : ").split())))

for i in range(1, n):
    for j in range(i + 1):
        # 해당 정수의 위치가 1열로 왼쪽 위의 수가 없을때
        if (j == 0): 
            a = 0
        else: 
            a = data[i - 1][j - 1]
        
        # 해당 정수의 위치가 마지막열로 오른쪽 위의 수가 없을때
        if (j == i): 
            b = 0
        else: 
            b = data[i - 1][j]
        
        # 최대값 산출
        data[i][j] += max(a, b)

print(max(data[n - 1]))