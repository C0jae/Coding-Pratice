from collections import deque

# deque() import 필요
queue = deque()

# 1추가 -> 3추가 -> 5추가 -> 삭제 -> 7추가 -> 9추가
queue.append(1)
queue.append(3)
queue.append(5)

queue.pop()

queue.append(7)
queue.append(9)

print(queue)    # [3, 5, 7, 9]