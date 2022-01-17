import heapq


def solution(food_times, k):
    # 음식을 먹을 때의 시간(초)
    cnt = 0
    
    # 음식순서(리스트 고려 0부터 시작 -> 결과값 도출시에는 i + 1번째 음식)
    i = 0
    
    # k초일때 먹을 순서
    while cnt <= k:
        # n번째 접시에 음식이 있을 경우 1초만큼 섭취 후 다음번호 음식으로 이동
        if (food_times[i] != 0):
            food_times[i] -= 1
            i += 1
            cnt += 1
        
        # n번째 접시에 음식이 없을 경우 다음번호 음식으로 이동  
        else:
            i += 1
        
        # 리스트 배열 고려 i가 food_times의 길이만큼 증가하였다면 0으로 재선언
        if (i == len(food_times)):
            i = 0

    # 결과값 도출을 위해 i = 0이라면 len(food_times) 번째 음식
    if (i == 0):
        i = len(food_times)
        
    return i



def solution2(food_times, k):
    # 음식 전체를 먹는 시간보다 k가 크다면 -1 리턴
    if (sum(food_times) <= k):
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    
    # 먹기 위해 사용한 시간
    sum_value = 0
    
    # 직전에 다 먹은 음식 시간
    previous = 0
    
    # 남은 음식의 갯수
    length = len(food_times)
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        # 가장 적은 개수의 음식 제외 및 now변수에 선언(음식 시간)
        now = heapq.heappop(q)[0]
        
        # 먹은 음식시간만큼 sum_value에 추가
        sum_value += (now - previous) * length
        
        # 음식 개수 -1
        length -= 1
        
        # 이전 음식 시간에 선언
        previous = now
        
    # 음식의 번호 기준으로 정렬
    result = sorted(q, key = lambda x: x[1])
    
    return result[(k - sum_value) % length][1]
    

food_times = [8, 6, 4]
k = 15

print(solution2(food_times, k))