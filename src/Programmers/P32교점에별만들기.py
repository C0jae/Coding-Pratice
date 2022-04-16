def solution(line):
    cross = []  # 교점 리스트
    crossX = [] # 교점 x좌표
    crossY = [] # 교점 y좌표
    
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            a = line[i][0]
            b = line[i][1]
            e = line[i][2]
            
            c = line[j][0]
            d = line[j][1]
            f = line[j][2]
            
            # 교점이 정수라면 cross 리스트에 추가하기
            if (a * d) != (b * c) and ((b * f) - (e * d)) % ((a * d) - (b * c)) == 0 and ((e * c) - (a * f)) % ((a * d) - (b * c)) == 0:
                x = int(((b * f) - (e * d)) / ((a * d) - (b * c)))
                y = int(((e * c) - (a * f)) / ((a * d) - (b * c)))
                
                cross.append((x, y))
                crossX.append(x)
                crossY.append(y)
    
    minX = min(crossX) if min(crossX) >= 0 else (-1 * min(crossX))
    minY = min(crossY) if min(crossY) >= 0 else (-1 * min(crossY))
    
    l = len(crossX)
    answer = [["."] * (max(crossX) - min(crossX) + 1) for _ in range((max(crossY) - min(crossY) + 1))]
    
    for i in range(l):
        answer[-crossY[i] + minY][crossX[i] + minX] = "*"
                
    return ["".join(ans) for ans in answer]

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

print(solution(line))