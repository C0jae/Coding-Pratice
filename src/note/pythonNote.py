from collections import deque


q = deque()

q.append((1, 2))
q.append((3, 4))
q.append((3, 5))

print(q)

if (1, 2) not in q:
    print("T")
else:
    print("F")