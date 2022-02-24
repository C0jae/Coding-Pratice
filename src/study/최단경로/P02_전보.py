import heapq

# 도시 개수, 통로 개수, 메시지를 보내고자 하는 도시 입력
n, m, c = map(int, input("n, m, c값 입력 : ").split())

# 도시별 연결되어있는 도시 및 전송시간을 나타내는 정보 그래프 선언
graph = [[] for _ in range(n + 1)]

# 초기값 설정
INF = int(1e9)
distance = [INF] * (n + 1)

# 도로정보 입력받아 graph리스트에 추가하기
for _ in range(m):
    x, y, z = map(int, input("x, y, z 값 입력 : ").split())
    graph[x].append((y, z))

def solution(c):
    q = []
    heapq.heappush(q, (0, c))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heqppush(q, (cost, i[0]))
                
solution(c)

count = 0
max_distance = 0

for i in distance:
    if i != INF:
        count += 1
        max_distance = max(max_distance, i)
        
print(count - 1, max_distance)