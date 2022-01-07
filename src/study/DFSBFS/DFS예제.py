# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드(시작지점)를 방문처리
    visited[v] = True
    
    # 방문한 노드 출력
    print(v, end = " ")
    
    for i in graph[v]:
        if (not visited[i]):
            dfs(graph, i, visited)
    
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
print(dfs(graph, 1, visited))