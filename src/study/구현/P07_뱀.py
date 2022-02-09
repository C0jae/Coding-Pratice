from collections import deque


n = int(input("보드 크기 n : "))
k = int(input("사과갯수 k : "))

# 맵 리스트 생성
data = [[0] * n for _ in range(n)]

# 사과가 존재하는 위치를 1로 선언
for _ in range(k):
    a, b = map(int, input("사과 위치 입력 행, 렬 : ").split())
    data[a - 1][b - 1] = 1

# 방향정보
l = int(input("방향 전환 횟수 : "))

# 방향정보 리스트
direction = []

# 방향정보 입력 direction[(x, c)]
for _ in range(l):
    x, c = input("초, 방향 정보 입력 : ").split()
    direction.append((int(x), c))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 시간
time = 0

# 초기 방향(오른쪽) -> dx[0], dy[0]
direct = 0
# 시작지점(0, 0)
x = 0
y = 0

# deque 이용 -> 이동할때마다 새로운 좌표(머리) 추가 and 몸 길이가 늘어나지 않는다면 가장 오래된 좌표(꼬리) 삭제
q = deque()
q.append((x, y))

# 방향정보의 인덱스 direction[d], direction[d]
d = 0

while True:
    # 방향 변경
    if time == direction[d][0]:
        # 왼쪽일 경우 dx, dy의 인덱스 값(direct) -1
        if direction[d][1] == "L":
            direct = (direct - 1) % 4

        # 오른쪽일 경우 dx, dy의 인덱스 값(direct) +1
        else:
            direct = (direct + 1) % 4
        
        # 현재 방향 변경한 정보를 알기위한 인덱스값 +1 direction[d]
        d = (d + 1) % l

    # 이동할 좌표 지정
    nx = x + dx[direct]
    ny = y + dy[direct]
    
    # 벽에 걸리지 않을경우
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
        # q에 똑같은 좌표가 존재할 경우(몸에 닿을경우)
        if (nx, ny) in q:
            # 닿았을 당시의 시간을 구해야 하므로 time +1 후에 종료
            time += 1
            break
        
        # 이동한 곳에 사과가 있을경우 -> 해당지점 사과 사라짐, 새로운 좌표추가 및 시간 +1
        if data[nx][ny] == 1:
            data[nx][ny] == 0
            q.append((nx, ny))
            x, y = nx, ny
            time += 1
        
        # 이동한 곳에 사과가 없을경우 -> 새로운 좌표추가 및 시간 +1, 가장 오래된 좌표(꼬리) 데이터 삭제
        else:
            q.append((nx, ny))
            q.popleft()
            x, y = nx, ny
            time += 1

    # 벽에 닿았을경우
    else:
        # 닿았을 당시의 시간을 구해야 하므로 time +1 후에 종료
        time += 1
        break

print(time)