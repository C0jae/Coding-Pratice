t = int(input("테스트 케이스 수 : "))

# 테스트케이스 수 만큼 반복
for i in range(t):
    n = int(input("크기 n : "))
    
    # 요금정보 저장
    graph = []
    for i in range(n):
        graph.append(list(map(int, input("각 칸의 비용 : ").split())))
        
    # (n + 2) x (n + 2) 크기의 리스트 선언 및 INF값 부여
    # 출발지점[1][1]은 graph[0][0]의 요금 값 부여
    INF = int(1e9)
    data = [[INF] * (n + 2) for _ in range(n + 2)]
    data[1][1] = graph[0][0]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            
            # 해당 장소의 상하좌우 장소 중 최소값 찾기 및 해당 최소값 + 현재 장소의 요금 적용
            minimum = min(data[i - 1][j], data[i + 1][j], data[i][j - 1], data[i][j + 1])
            data[i][j] = minimum + graph[i - 1][j - 1]
    
    # 도착장소의 최소 요금 출력 n행 n렬
    print(data[n][n])