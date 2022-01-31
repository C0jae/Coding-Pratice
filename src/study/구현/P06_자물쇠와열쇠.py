# 열쇠로 자물쇠를 열 수 없는 경우(열쇠의 돌기 갯수 < 자물쇠 홈 개수)
def fail(key, lock):
    a = 0
    b = 0
    
    for i in range(len(key)):
        a += key[i].count(1)
        
    for i in range(len(lock)):
        b += lock[i].count(0)
    
    if a < b:
        return False


# 시계방향 90도 회전
def turn_90(key):
    # 행의 길이
    n = len(key)
    # 열의 길이
    m = len(key[0])
    
    data = [[0] * n for _ in range(m)]
    
    # 90도 회전한 값을 data에 대입
    for i in range(n):
        for j in range(m):
            data[j][n - i - 1] = key[i][j]
    
    return data


# 자물쇠 부분이 모두 1인지 확인(a = 0부터 len(big_lock) - 1 까지)
def success(key, big_lock, a, b):
    n = len(big_lock)
    m = len(key)
    
    # 자물쇠 + 열쇠를 나타내는 sum_lock 생성
    sum_lock = [[0] * n for _ in range(n)]
    
    # sum_lock = big_lock
    for i in range(n):
        for j in range(n):
            sum_lock[i][j] = big_lock[i][j]
    
    # sum_lock + key
    for i in range(m):
        for j in range(m):
            sum_lock[a + i][b + j] += key[i][j]
        
    # sum_lock의 자물쇠 위치 부분이 전부 1인지 확인
    for i in range(n // 3):
        for j in range(n // 3):
            # 1이라면 다음 항목 검사
            if sum_lock[i + (n // 3)][j + (n // 3)] == 1:
                continue
            # 하나라도 1이 아니라면 false 리턴
            else:
                return False
            
    # 전부 1로 반복문을 빠져나올경우 true 리턴
    return True      
    

def solution(key, lock):
    fail(key, lock)
    
    n = len(lock)
    m = len(key)
    
    # lock 길이의 x3 인 크기의 big_lock 생성
    big_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    # lock의 모양이 big_lock의 가운데에 오도록 설정
    for i in range(n):
        for j in range(n):
            big_lock[i + n][j + n] = lock[i][j]
    
    # key를 이동하면서 lock과 맞춰보기
    # 세로이동     
    for i in range(1, 2 * n):
        # 가로이동
        for j in range(1, 2 * n):
            # 4방향 회전
            for _ in range(4):
                # 맞물릴경우 true 리턴
                if success(key, big_lock, j, i) == True:
                    return True
                
                # 다를경우 90도 회전
                else:
                    key = turn_90(key)
    
    # true가 리턴되지 않았을경우(맞는곳이 없을경우) false 리턴
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

if solution(key, lock) == True:
    print("true")

else:
    print("false")