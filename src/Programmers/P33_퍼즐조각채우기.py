
# 4방향 탐색(i값, j값, 테이블 종류, 빈칸표시, 빈칸 좌표)
def direction(a, b, data, x, d):
    if data[a][b] != x:
        return
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    d.append((a, b))
    
    for i in range(4):
        nx = dx[i] + a
        ny = dy[i] + b
        
        if data[nx][ny] == x:
            d.append((nx, ny))
            
            direction(nx, ny, data, x)
        
    return d

# 빈공간 찾기 함수 game_board
def search_empty(game_board):
    result = []
    l = len(game_board)
    
    for i in range(l):
        for j in range(l):
            d = []
            direction(i, j, game_board, 0, d)
                
    
    return result

# 블록찾기 함수 table

# 시작지점 좌표 (0, 0) 기준으로 변경

# 블럭 회전

def solution(game_board, table):
    answer = -1
    
    empty = []
    block = []
    
    return answer


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]