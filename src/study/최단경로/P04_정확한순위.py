from collections import deque


n, m = map(int, input("학생수, 비교할 횟수 : ").split())

q = deque()

# a, b값 입력받으면서 q에 데이터 입력
for _ in range(m):
    a, b = map(int, input("A, B 값 입력 : ").split())
    q.append((a, b))

# 길이 n + 1인 리스트 생성
data = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, len(data)):
    for j in range(0, len(data)):
        # 같은 행렬(같은학생)인 곳은 2로 표시
        if i == j:
            data[i][j] = 2
        
        # 0열은 3으로 표시(필요 없는 범위) => 결과값 출력하기 위해
        if j == 0:
            data[i][j] = 3

# 입력된 성적비교 데이터 하나하나 적용
while q:
    a, b = q.popleft()
    
    data[a][b] = 1  # a학생이 b학생보다 성적이 낮다 => 1 입력
    data[b][a] = -1 # b학생이 a학생보다 성적이 높다 => -1 입력
    
    for i in range(1, len(data)):
        # b학생보다 성적이 높은 학생이 있는경우
        if data[b][i] == 1:
            data[a][i] == 1 # a학생보다도 점수가 높다
            data[i][a] == -1
        
        # a학생보다 성적이 낮은 학생이 있는경우
        if data[i][a] == 1:
            data[i][b] = 1  # b학생보다도 점수가 낮다
            data[b][i] = -1
        
result = 0

# 각 행을 조사하여(각 학생을 조사하여) 해당 행에 0이 없다면
# (다른 학생과의 높고 낮음의 정보가 있다 => 자신의 순위를 알 수 있음) result +1
for i in range(1, len(data)):
    print(data[i])
    if 0 not in data[i]:
        result += 1
    
print(result)   # 결과출력