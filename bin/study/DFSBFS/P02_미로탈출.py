from collections import deque

n, m = map(int, input("n, m 값 입력 : ").split())

maze = []
for i in range(n):
    maze.append(list(map(int, input("괴물 여부 입력 : "))))
    
# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y):
    queue = deque()
    queue.append((x, y))
    
    # queue가 빌때까지 반복 -> for문을 전부 돌았음에도 continue만 적용되었을 경우(4가지 방향에 갈 곳이 없을 경우)
    while queue:
        # 이동한 좌표를 x, y에 새로 가져오기
        x, y = queue.popleft()
      
        # 4방향 모두 검사
        for i in range(4):
            # 검사할 좌표 설정
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어난 경우 무시
            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            
            # 이동방향에 괴물이 있다면( == 0 ) 무시
            if (maze[nx][ny] == 0):
                continue
            
            # 이동할 수 있는 칸일경우
            if (maze[nx][ny] == 1):
                # 이동할때마다 횟수 표시(결과값)
                maze[nx][ny] = maze[x][y] + 1
                # 이동할 좌표를 queue에 할당
                queue.append((nx, ny))
    
    return maze[n - 1][m - 1]

print(move(0, 0))