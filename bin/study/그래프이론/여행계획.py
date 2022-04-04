# 서로소 집합 알고리즘 이용

# 공통 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

# 연결되어 있는 집합끼리 값 통일하기
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        

n, m = map(int, input("여행지 n, 도시수 m : ").split())

# 도시끼리의 연결정보 입력받기
data = []
for i in range(n):
    data.append(list(map(int, input("연결 정보 입력 : ").split())))

# 여행계획 정보 입력받기
plan = list(map(int, input("여행 계획 입력 : ").split()))

# 서로소 집합 알고리즘을 위한 리스트 선언 parent[1] = 1, parent[2] = 2 ...
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

# 연결되어 있는 도시의 정보를 찾으면(data[i][j] == 1) 값 통일시키기
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            union(parent, i + 1, j + 1)

# 여행계획에 있는 도시들의 값이 모두 같으면(모두 이동할 수 있으면) True, 아니면(하나라도 이동할 수 없으면) False 선언
result = True
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

if result:
    print("YES")
else:
    print("NO")