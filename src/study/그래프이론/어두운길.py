# 연결되어있는 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]

# 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input("집, 깅 수 입력 : ").split())

datas = []  # 거리, 집1, 집2의 정보들 저장
money = 0   # 최소비용

parent = [0] * (m + 1)
for i in range(1, m + 1):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input("집1, 집2, 거리 입력 : ").split())
    datas.append((z, x, y))
    money += z

datas.sort()

for data in datas:
    z, a, b = data
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        money -= z

print(money)