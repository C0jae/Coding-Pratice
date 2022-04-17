def solution(line):
    cross = []  # 교점 리스트
    crossX = [] # 교점 x좌표
    crossY = [] # 교점 y좌표
    
    # 두 직선의 교점 구하기
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            # 직선1
            a = line[i][0]
            b = line[i][1]
            e = line[i][2]
            
            직선2
            c = line[j][0]
            d = line[j][1]
            f = line[j][2]
            
            if a * d == b * c:
                continue
            
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))
            
            # 교점이 정수라면 cross 리스트에 추가하기
            if x == int(x) and y == int(y):
                cross.append((int(x), int(y)))
                crossX.append(int(x))
                crossY.append(int(y))
    
    minX = min(crossX)
    maxX = max(crossX)
    minY = min(crossY)
    maxY = max(crossY)
    
    answer = ['.' * (maxX - minX + 1)] * (maxY - minY + 1)
    
    for c in cross:
        x, y = c
        answer[maxY - y] = answer[maxY - y][:x - minX] + '*' + answer[maxY - y][x - minX + 1:]
    
    return answer

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

print(solution(line))