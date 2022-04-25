from collections import deque


# 4방향 탐색(i값, j값, 테이블 종류, 빈칸표시, 빈칸 좌표)
def direction(a, b, data, x, d):
    if data[a][b] != x:
        return
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    d.append([a, b])
    
    dq = deque()
    dq.append([a, b])
    
    data[a][b] = 2
    
    while dq:
        a, b = dq.popleft()
        
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            
            if nx >= 0 and ny >= 0 and nx < len(data) and ny < len(data) and data[nx][ny] == x:
                d.append([nx, ny])
                dq.append([nx, ny])
                
                data[nx][ny] = 2
        
    return d

# 빈공간 찾기 함수 game_board
def search_empty(game_board):
    l = len(game_board)
    empty = []
    
    for i in range(l):
        for j in range(l):
            d = []
            direction(i, j, game_board, 0, d)
            
            if len(d) > 0:
                empty.append(d)
    
    return empty

# 블록찾기 함수 table
def search_block(table):
    l = len(table)
    block = []
    
    for i in range(l):
        for j in range(l):
            d = []
            direction(i, j, table, 1, d)
            
            if len(d) > 0:
                block.append(d)
    
    return block

# 시작지점 좌표 (0, 0) 기준으로 변경
def reset(data):
    for i in range(len(data)):
        a = data[i][0][0]   # 도형 하나의 첫 기준 좌표 a (a, b)
        b = data[i][0][1]   # 도형 하나의 첫 기준 좌표 b (a, b)
        
        for j in range(len(data[i])):   # 도형의 기준을 (0, 0)으로 변동하기(이동)
            data[i][j][0] -= a
            data[i][j][1] -= b
            
    return data

# 블럭 회전
def rotation(oneBlock):
    n = max(len(oneBlock), len(oneBlock[0]))
    rot = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rot[j][n - 1 - i] = oneBlock[i][j]
    
    a = 0
    b = n - 1
    print(rot)
    
    return rot

def solution(game_board, table):
    result = []
    
    empty = search_empty(game_board)    # 빈칸이 위치한 좌표
    block = search_block(table)         # 블록이 위치한 좌표
    
    empty = reset(empty)    # 모든 빈칸 영역의 기준칸 좌표가 (0, 0)으로 오도록 좌표 조정
    block = reset(block)    # 모든 블록의 기준칸 좌표가 (0, 0)으로 오도록 좌표 조정
    
    # print(empty)
    # print(block)
    # print("---------------")
    
    for i in range(len(empty)):
        for j in range(len(block)):
            # print(i, j, empty[i], block[j])
            if empty[i] == block[j]:
                # print("1", empty[i])
                result.append(empty[i])
                break
            else:
                for k in range(3):
                    block[j] = rotation(block[j])
                    # print("empty :", empty[i], ":", " rot",k,":",block[j])
                    if empty[i] == block[j]:
                        # print("2", empty[i])
                        result.append(empty[i])
                        break
    answer = 0
    for i in range(len(result)):
        answer += len(result[i])
                        
    return answer


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board, table))