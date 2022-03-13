from collections import deque


def solution(board):
    # board 외벽 둘러싸기
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    q = deque([(1, 1), (1, 2), 0])  # 첫번재 좌표, 두번째 좌표, 시간
    check = set([(1, 1), (1, 2)])   # 방문 확인용
    
    while q:
        loc1, loc2, time = q.popleft()
        
        if loc1 == (n, n) or loc2 == (n, n):
            return time
        
def move(loc1, loc2, new_board):
    x, y = 0, 1
    cand = []
    
    # 평행이동
    dic = {0:[-1, 0], 1:[1, 0], 2:[0, 1], 3:[0, -1]}
    for i in range(4):
        nx1 = (loc1[x] + dic[i][0], loc1[y] + dic[i][1])
        nx2 = (loc2[x] + dic[i][0], loc2[y] + dic[i][1])
        
        if new_board[nx1[x]][nx1[y]] == 0 and new_board[[nx2[x]][nx2[y]] == 0:
            cand.append((nx1, nx2))
    
    # 회전
        
    
    
    return robot

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

solution(board)