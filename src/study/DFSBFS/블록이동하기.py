from collections import deque


def solution(board):
    # board 외벽 둘러싸기
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    
    # board에 외벽을 둘러싼 new_board 생성
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    q = deque( [ ((1, 1), (1, 2), 0) ] )  # 첫번재 좌표, 두번째 좌표, 시간
    check = set( [ ((1, 1), (1, 2)) ] )   # 방문 확인용 집합
    
    while q:
        loc1, loc2, time = q.popleft()  # 좌표1, 좌표2, 시간
        
        # 두개의 좌표중 하나라도 (n, n)에 도달시 종료
        if loc1 == (n, n) or loc2 == (n, n):
            return time
        
        # 이동 가능한 좌표들 중 아직 방문하지 않은 좌표가 있을 경우(not in check) 해당 좌표와 시간을 q와 check에 추가한후 while문 반복
        for mov in move(loc1, loc2, new_board):
            if mov not in check:
                q.append((mov[0], mov[1], time + 1))
                check.add(mov)
        
def move(loc1, loc2, new_board):
    x, y = 0, 1 # 좌표 행, 열 값의 인덱스
    can = []
    
    # 평행이동
    dic = {0:[-1, 0], 1:[1, 0], 2:[0, 1], 3:[0, -1]}    # 4가지 방향에 대한 key:value 값 생성(상, 하, 우, 좌)
    for i in range(4):
        nx1 = (loc1[x] + dic[i][0], loc1[y] + dic[i][1])
        nx2 = (loc2[x] + dic[i][0], loc2[y] + dic[i][1])
        
        # 평행이동을 한 좌표가 전부 벽이 아닐경우( == 0 ) can 리스트에 해당 좌표 추가
        if new_board[nx1[x]][nx1[y]] == 0 and new_board[nx2[x]][nx2[y]] == 0:
            can.append((nx1, nx2))
    
    # 회전
    # 두개의 좌표가 평행일경우( = 같은 행일 경우)
    if loc1[x] == loc2[x]:
        up, down = -1, 1    # 행의 이동
        # 회전이 가능한 범위일 경우 can에 이동하는 좌표 추가
        # 아래로 회전할 경우 기존 좌표 2개의 밑 좌표가 모두 뚫려 있어야 하며, 위로 회전할 경우 기존 좌표 2개의 위 좌표가 모두 뚫려 있어야 한다.
        for d in [up, down]:
            if new_board[loc1[x] + d][loc1[y]] == 0 and new_board[loc2[x] + d][loc2[y]] == 0:
                can.append( ( loc1, (loc1[x] + d, loc1[y]) ) )  # loc1 좌표를 중심으로 회전한 좌표
                can.append( ( loc2, (loc2[x] + d, loc2[y]) ) )  # loc2 좌표를 중심으로 회전한 좌표

    # 두개의 좌표가 수직일 경우( = 같은 열일 경우)
    else:
        left, right = -1, 1
        # 왼쪽으로 회전할 경우 기존 좌표 2개의 왼쪽 좌표가 모두 뚫려 있어야 하며, 오른쪽으로 회전할 경우 기존 좌표 2개의 오른쪽 좌표가 모두 뚫려 있어야 한다.
        for d in [left, right]:
            if new_board[loc1[x]][loc1[y] + d] == 0 and new_board[loc2[x]][loc2[y] + d] == 0:
                can.append(((loc1[x], loc1[y] + d), loc1))  # loc1 좌표를 중심으로 회전한 좌표
                can.append(((loc2[x], loc2[y] + d), loc2))  # loc2 좌표를 중심으로 회전한 좌표
            
    return can  # 기준 좌표에서 이동할 수 있는 장소의 모든 좌표들 값을 리턴

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

print(solution(board))



# def solution(board):
    
#     n = len(board)
#     new_board = [[1] * (n + 2) for _ in range(n + 2)]
    
#     for i in range(n):
#         for j in range(n):
#             new_board[i + 1][j + 1] = board[i][j]
            
#     q = deque( [ ((1, 1), (1, 2), 0) ] )
#     check = set( [ ((1, 1), (1, 2)) ] )
    
#     while q:
#         loc1, loc2, time = q.popleft()
        
#         if loc1 == (n, n) or loc2 == (n, n):
#             return time
        
#         for mov in move(loc1, loc2, new_board):
#             if mov not in check:
#                 q.append((mov[0], mov[1], time + 1))
#                 check.add(mov)
            
            
# def move(loc1, loc2, new_board):
#     can = []
    
#     dic = {0:[-1, 0], 1:[1, 0], 2:[0, -1], 3:[0, 1]}
#     for i in range(4):
#         nx1 = (loc1[0] + dic[i][0], loc1[1] + dic[i][1])
#         nx2 = (loc2[0] + dic[i][0], loc2[1] + dic[i][1])
        
#         if new_board[nx1[0]][nx1[1]] == 0 and new_board[nx2[0]][nx2[1]] == 0:
#             can.append( (nx1, nx2) )
    
#     if loc1[0] == loc2[0]:
#         up, down = -1, 1
        
#         for d in [up, down]:
#             if new_board[loc1[0] + d][loc1[1]] == 0 and new_board[loc2[0] + d][loc2[1]] == 0:
#                 can.append( ( loc1, (loc1[0] + d, loc1[1]) ) )
#                 can.append( ( loc2, (loc2[0] + d, loc2[1]) ) )
    
#     else:
#         left, right = -1, 1
        
#         for d in [left, right]:
#             if new_board[loc1[0]][loc1[1] + d] == 0 and new_board[loc2[0]][loc2[1] + d] == 0:
#                 can.append( (loc1 ,(loc1[0], loc1[1] + d) ) )
#                 can.append( (loc2 ,(loc2[0], loc2[1] + d) ) )
    
#     return can


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

print(solution(board))