# solution 함수 적용
def solution(x, y):
    # 검사 범위가 해당 배열을 넘어가는 순간 종료
    if (x <= -1 or x >= n or y <= -1 or y >= m):
        return False
    
    # 검사지점이 방문하지 않은지점(0) 이라면 해당지점을 1로 변경 및 상하좌우 지점도 검사 진행
    if (graph[x][y] == 0):
        # 1로 변경하여 같은지점을 다시 검사하는 일이 발생하지 않게한다.
        graph[x][y] = 1
        
        # 상하좌우 검사 진행
        solution(x - 1, y)
        solution(x + 1, y)
        solution(x, y - 1)
        solution(x, y + 1)
        
        # 모든 검사가 끝난 후 true 리턴
        return True
    
    # 검사지점이 방문한 지점이라면(1) false리턴 및 종료
    return False


n, m = map(int, input("행, 렬 입력 : ").split())

graph = []

for i in range(n):
    graph.append(list(map(int, input("입력 : "))))
    
count = 0

# 모든 지점을 검사(solution)할 수 있도록 반복문 적용
for i in range(n):
    for j in range(m):
        # 검사 결과가 true라면 count + 1
        if (solution(i, j) == True):
            count += 1

# 결과값 출력        
print(count)