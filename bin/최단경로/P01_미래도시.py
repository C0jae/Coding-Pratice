# 무한값 설정
INF = int(1e9)

# 회사 수 n, 도로 수 m 값 입력
n, m = map(int, input("n, m값 입력 : ").split())

# 도로와 도로의 정보를 담을수 있는 2차원 배열 리스트 생성(초기값 : INF)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 같은지점에 해당하는(이동하지 않는) 지점은 0으로 재설정
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 연결되어 있는 도로를 입력받아 해당지점의 정보를 1로 재 설정            
for _ in range(m):
    i, j = map(int, input("도로 정보 입력 : ").split())
    graph[i][j] = 1
    graph[j][i] = 1
    
# 거쳐갈 도시 x, 최종 목적지 k 값 입력        
x, k = map(int, input("x, k값 입력 : ").split())

# 플로이드 워셔 알고리즘 이용
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 1번 -> k로의 최단거리 + k -> x로의 최단거리 계산
distance = graph[1][k] + graph[k][x]

# 정답 출력
if distance >= INF:
    print(-1)
else:
    print(distance)