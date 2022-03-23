# 2개의 최소 신장 트리 만들기 => 크루스칼 알고리즘
# 서로소 알고리즘
# 최소 신장 트리를 구성하는 간선(요금) 중에서 가장 큰 간선(요금)을 제거 -> 2개의 간선이 만들어지면서 최소비용이 된다.

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union의 연산)의 개수 입력받기    
v, e = map(int, input("노드와 간선의 수 : ").split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용(가장 큰 비용)을 담을 변수 선언
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input("집 a, b / 금액 : ").split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0    # 최소 신장 트리에 포함되는 간선 중에서 가장 비용기 큰 간선

# 간선을 하나씩 확인하기
for edge in edges:
    cost, a, b = edge
    
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)



# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
    
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
    
# n, m = map(int, input("n, m 값 입력 : ").split())

# parent = [0] * (n + 1)
# for i in range(1, n + 1):
#     parent[i] = i

# edges = []
# result = 0

# for _ in range(m):
#     a, b, cost = map(int, input("a, b, cost값 입력 : ").split())
#     edges.append((cost, a, b))

# edges.sort()
# last = 0

# for edge in edges:
#     cost, a, b = edge
    
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         last = cost

# print(result - last)