# 방향정보
l = int(input("방향 전환 횟수 : "))

# 방향정보 리스트
direction = []

# 방향정보 입력
for _ in range(l):
    x, c = input("초, 방향 정보 입력 : ").split()
    direction.append((int(x), c))

print(direction[0][0])