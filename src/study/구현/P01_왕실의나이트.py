p = input("기사 위치 : ")

# 기사의 위치 배열화(x, y) 및 x위치값 아스키 코드로 변경
data = [0] * 2
data[0] = ord(p[0])
data[1] = int(p[1])

# 이동 가능한 경로
way = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 최대 이동경로
cnt = 0

for i in way:
    # 아스키코드 => a : 97  / h : 104
    if (data[0] + i[0] >= 97 and data[0] + i[0] <= 104 and data[1] + i[1] >= 1 and data[1] + i[1] <= 8):
        cnt += 1

print(cnt)
