n = int(input("도시 수 : "))    # 도시 개수 입력
m = int(input("버스 수 : "))    # 버스 개수 입력

# 최소비용을 나타내는 리스트 선언 및 초기값 INF로 설정(노선이 없는곳은 INF 이상으로 설정하기 위함)
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 버스 정보를 통한 출발 도시와 도착 도시의 요금값 입력(직행 기준)
for _ in range(m):
    a, b, c = map(int, input("버스 정보 입력 : ").split())
    if c < graph[a][b]:
        graph[a][b] = c 

# 출발도시와 도착도시가 같은 지점은 0으로 표시(이동 요금 없음)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜 알고리즘 이용(직행과 직통중에 무엇이 더 싼지)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 요금 정보를 출력조건에 맞게 출력            
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 노선이 없는 경우 0 출력
        if graph[i][j] >= INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
        
    print()