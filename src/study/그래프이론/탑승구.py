def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
g = int(input("탑승구 갯수 : "))
p = int(input("비행기 갯수 : "))

# 0번부터 g번의 게이트 생성(0번 게이트 : 가상의 게이트)
parent = [0] * (g + 1)

for i in range(1, g + 1):
    parent[i] = i

result = 0

for _ in range(p):
    data = find_parent(parent, int(input("비행기 정보 입력 : ")))
    
    if data == 0:
        break
    
    union_parent(parent, data, data - 1)
    result += 1
    
print(result)