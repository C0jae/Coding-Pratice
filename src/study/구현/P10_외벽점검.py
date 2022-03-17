from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)  # 취약지점의 수
    
    # 원형의 장소를 일자로 변경하여(취약지점 + n으로 표시지점 2배) 취약지점 표시
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 친구들의 수(모두 점검해야 할 경우를 초기값으로 설정)
    answer = len(dist) + 1
    
    for start in range(length):
        # permutations => nPr n개의 수 중 r개의 조합(중복 허용 => (a, b) != (b, a))
        for friends in list(permutations(dist, len(dist))):
            count = 1
            # 해당 취약지점에서 특정 친구가 갈 수 있는 최대 거리 계산
            position = weak[start] + friends[count - 1]
            
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    
                    position = weak[index] + friends[count - 1]
                
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
    
    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]