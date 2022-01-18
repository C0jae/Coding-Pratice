from collections import deque


n, m, k, x = map(int, input("입력 : ").split())

# 0번 ~ n번 도시까지 도시별 연결된 도시의 정보를 담는 리스트 선언
graph = [[] for _ in range(n + 1)]

# 도시별 연결된 도시의 정보 입력
for _ in range(m):
    a, b = map(int, input("도로정보 입력 : ").split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거릐 초기화
distance = [-1] * (n + 1)

# 출발 도시까지의 거리는 0으로 설정
distance[x] = 0

# 너비 우선 탐색(BFS) 수행
q = deque([x])

while q:
    now = q.popleft()
    # print("graph[", now, "] : ", graph[now])
    
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시의 경우
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# print(distance)
# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
        
# 최단거리가 k인 도시가 없다면 -1 출력
if check == False:
    print(-1)