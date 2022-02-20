from collections import deque


n, k = map(int, input("n, k 입력 : ").split())

# 바이러스 분포 리스트 표시
graph = []

# 바이러스에 대한 정보 리스트 표시
data = []

for i in range(n):
    # 바이러스 리스트 입력
    graph.append(list(map(int, input("바이러스 분포 정보 입력 : ").split())))
    
    for j in range(n):
        # 바이러스가 존재하는 지점에 대한 정보를 data 리스트에 추가
        if graph[i][j] != 0:
            # 바이러스 종류, 시간(0초), 지점(i, j) 정보 추가
            data.append((graph[i][j], 0, i, j))

# 낮은 번호의 바이러스부터 증식 되므로 data를 정렬
data.sort()
q = deque(data)

# 구하려는 시간과 지점 입력
target_s, target_x, target_y = map(int, input("s, x, y 입력 : ").split())

# 상하좌우 위치 지정
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# q의 정보가 빌때까지 반복
while q:
    virus, s, x, y = q.popleft()
    
    # s초가 지날경우 break
    if s == target_s:
        break
    
    # 4방향 확인 및 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 이동 가능한 장소이며 바이러스 증식이 안되었을 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                # 신규 바이러스 정보 수정
                graph[nx][ny] = virus
                # 신규 바이러스 증식에 대한 정보 q에 추가
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])