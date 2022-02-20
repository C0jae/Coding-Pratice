from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의(가장 오래된(?)) 원소를 뽑아내 출력
        v = queue.popleft()
        print(v, end = " ")
        
        # 해당 원소와 연결되었으며 방문하지 않은 원소를 큐에 삽입후 방문처리
        for i in graph[start]:
            if (not visited[i]):
                queue.append(i)
                visited[i] = True

# 1부터 8번 노드까지 인접해 있는 노드를 2차원 배열로 표현
graph = [
    [],         # index 0부터 시작하므로 임의의 빈 배열 생성
    [2, 3, 8],  # 1번 노드
    [1, 7],     # 2번 노드
    [1, 4, 5],  # 3번 노드
    [3, 5],     # 4번 노드
    [3, 4],     # 5번 노드
    [7],        # 6번 노드
    [2, 6, 8],  # 7번 노드
    [1, 7],     # 8번 노드
]

# 아직 방문한 노드가 없으므로 모든 노드에 대한 정보를 false로 표현
# 시작지점이거나 방문하였을 경우 True로 변경(dfs함수에서 진행)
visited = [False] * 9

# 결과값 출력 (작은 값의 노드부터 출발로 약속)
print(bfs(graph, 1, visited))