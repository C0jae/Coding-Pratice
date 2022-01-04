t = int(input("횟수 t 입력 : "))

# 각 테스트별 결과값 저장을 위한 배열 선언
result = [0] * t

for cnt in range(t):
    
    # 행렬값 입력
    n, m = map(int, input("n, m 값 입력 : ").split())

    # 각 행렬별 금 크기 입력
    gold = list(map(int, input("금 크기 입력 : ").split()))

    # 행렬값에 맞는 배열 선언
    data = [[0] * m for i in range(n)]

    # 금광의 자리별 크기를 배열에 지정
    a = 0
    for i in range(n):
        for j in range(m):
            data[i][j] = gold[a]
            a += 1

    # j행 i+1열의 최고값 = j행 i+1열의 금크기 + max(j-1행 i열, j행 i열, j+1행 i열)
    for i in range(m - 1):
        for j in range(n):
            # 첫번째 행으로 위에 금광이 없을경우
            if (j == 0):
                data[j][i + 1] += max(data[j][i], data[j + 1][i])
            
            # 위아래 금광이 전부 있을경우
            elif (j == n - 1):
                data[j][i + 1] += max(data[j - 1][i], data[j][i])
            
            # 마지막 행으로 밑에 금광이 없을경우
            else:
                data[j][i + 1] += max(data[j - 1][i], data[j][i], data[j + 1][i])
         
    maxgold = 0

    # 마지막 열의 표시값중 최대값이 해당 금광에서 얻을 수 있는 최대 금 크기
    for i in range(n - 1):
        maxgold = max(data[i][m - 1], data[i + 1][m - 1])
    
    # 각 금광마다 금의 최대값을 result 배열에 저장
    result[cnt] = maxgold

# 리스트 출력 
for i in result:
    print(i)