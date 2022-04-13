from itertools import permutations


# 탐사할 수 있는 던전 갯수 체크
def check(k, dungeons):
    cnt = 0
    
    for dungeon in dungeons:
        a, b = dungeon
        
        # 최소 피로도보다 적으면 return
        if k < a: return cnt
        
        k -= b      # 소모피로도
        cnt += 1    # 던전 탐사갯수 +1
    
    return cnt
        

def solution(k, dungeons):
    answer = []
    
    # 던전 탐사 순서의 모든 경우 정리
    data = permutations(dungeons, len(dungeons))
    
    # 각 탐사경로마다 탐사가능 갯수 answer리스트에 추가
    for d in data:
        answer.append(check(k, d))
        
    # 탐사던전 횟수가 가장 큰 수 출력
    return max(answer)

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))