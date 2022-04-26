def find_parent(parent, x):
    if parent[x] != x:
        x = parent[x]
        find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def solution(n, wires):
    wires.sort()
    result = []
    
    # 경로를 하나씩 끊어보기 위한 반복문
    for i in range(len(wires)):
        parent = [0] * (n + 1)
        for k in range(n + 1):
            parent[k] = k
        
        # 하나의 경로는 무시하기(= 끊기)
        for j in range(len(wires)):
            if i == j:
                continue
                
            union_parent(wires[j][0], wires[j][1], parent)
        
        # print(i, parent)
        a = parent.count(1)
        b = len(parent) - a - 1
        
        result.append(abs(a - b))
    
    # print(result)
    return min(result)

n = 6
wires = [[1, 4], [3, 6], [2, 5], [1, 5], [3, 5]]
# n = 9
# wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

print(sorted(wires))
print(solution(n, wires))