from collections import deque


n, l, r = map(int, input("크기n, l, r 값 입력 : ").split())

field = []  # 나라별 인구정보 리스트

for _ in range(n):
    field.append(list(map(int, input("인구 정보 : ").split())))
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]  # 행
dy = [0, 1, 0, -1]  # 열

# 인접한 국가의 연합가능 여부 검사
def check(x, y, index):
    # 연합하는 국가의 정보(좌표) 입력
    country = []
    country.append((x, y))
    
    q = deque()
    q.append((x, y))
    
    union[x][y] = index     # 해당 국가의 연합여부 및 소속그룹
    summary = field[x][y]   # 연합한 국가들의 총 인구
    count = 1               # 현재 연합한 국가 수
    
    while q:
        x, y = q.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 탐색좌표가 범위 내 이면서 탐색대상 국가가 연합소속이 없을 경우 실행
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 인구 차이가 조건범위 이내일 경우
                if l <= abs(field[nx][ny] - field[x][y]) <= r:
                    q.append((nx, ny))
                    
                    union[nx][ny] = index       # 연합번호 부여
                    summary += field[nx][ny]    # 인구수 추가
                    count += 1                  # 연합 국가 수 + 1
                    country.append((nx, ny))    # 연합 국가 정보 추가
    
    # 연합한 국가들의 인구 배분                
    for i, j in country:
        field[i][j] = summary // count
    
    return count

cnt = 0

# 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]    # 연합번호 리스트(초기 = -1)
    index = 0
    
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:   # 연합 소속이 아니라면 주변 국가 탐색
                check(i, j, index)  # 하나의 연합그룹 생성
                index += 1          # 다음 연합그룹 번호를 위한 index + 1
            
    if index == n * n:
        break
        
    cnt += 1

print(cnt)