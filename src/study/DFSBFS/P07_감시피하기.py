from collections import deque


# 감시 여부 체크    
def check(graph, x, y):
    # 4방향 체크
    for i in range(4):
        # 장애물과 학생이 없다면 같은방향으로 끝까지 계속해서 탐색
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 벽까지 확인했을 경우 while문 종료 후 다음방향 탐색
            if (nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            
            # 학생을 발견할경우 바로 False 리턴
            if graph[nx][ny] == "S":
                print("학생발견 :", graph[nx][ny])
                return False
            # 기둥을 발견할 경우 while문 종료 후 다음방향 탐색
            elif graph[nx][ny] == "O":
                break
            # 아무도 없거나 다른 선생님을 발견할 경우 같은방향 다음칸 탐색
            else:
                if i % 2 == 0:
                    dx[i] += 1
                else:
                    dy[i] += 1
    
    # 한명의 학생도 발견하지 못하였을 경우 True 리턴
    return True    


# 모든 선생님들의 위치에서 학생 체크                    
def all_check(graph, teacher):
    count = 0
    for i in range(len(teacher)):
        # 선생님 한명이 감시할 수 있는 범위 체크
        result = check(graph, teacher[i][0], teacher[i][1])
        
        # 학생을 발견하지 못할경우 count +1
        if result == True:
            count += 1
            
            # 모든 선생님이 학생을 발견하지 못하였을경우 True 리턴
            if count == len(teacher):
                return True
        # 한명이라도 학생을 발견한 경우 False 리턴    
        else:
            return False


n = int(input("n값 입력 : "))

graph = []
teacher = []

# 행 이동(북동남서)
dx = [-1, 0, 1, 0]
# 열 이동(북동남서)
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(input("복도 정보 입력 : ").split())
    for j in range(n):
        if graph[i][j] == "T":
            teacher.append((i, j))

# 기둥 위치를 저장하는 q선언
q = deque()
dq = deque()
result = 0

# 기둥 위치 선별
for i in range(n):
    for j in range(n):
        if graph[i][j] == "X":
            graph[i][j] == "O"
            
            q.append((i, j))
            
            # 기둥 3개의 위치가 모두 정해졌을 경우
            if len(q) == 3:
                # 모든 선생님들의 감시에서 학생이 발견되지 않을 경우 "YES" 출력 후 반복문 종료
                if all_check(graph, teacher):
                    result = 1
                    break
                # 학생이 발견된다면 기둥 위치 초기화
                else:
                    for z in range(3):
                      graph[q[i][0]][q[i][1]] == "X"


if result == 1:
    print("YES")
else:
    print(result)
    print("NO")