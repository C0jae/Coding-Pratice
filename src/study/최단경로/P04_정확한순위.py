from collections import deque


n, m = map(int, input("학생수, 비교할 횟수 : ").split())

q = deque()

for _ in range(m):
    a, b = map(int, input("A, B 값 입력 : ").split())
    q.append((a, b))

INF = int(1e9)
data = [[0] * (n + 1) for _ in range(n + 1)]

while q:
    a, b = q.popleft()
    