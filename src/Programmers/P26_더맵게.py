import heapq

def solution(scoville, k):
    answer = 0
    heap = []
    
    # scoville의 값들을 heapq 리스트에 적용(자동으로 오름차순 정렬 및 처리용이)
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            answer += 1
        except IndexError:
            return -1
        
    return answer

def solution2(scoville, k):
    answer = 0
    
    while True:
        # scoville 리스트 오름차순 정렬
        scoville.sort()
        
        # 해당 리스트의 길이가 1이면서 k보다 작으면 answer = -1 설정 및 break
        if (len(scoville) == 1 and scoville[0] < k):
            answer = -1
            break
        
        # 첫번째 수가(가장 작은 수) k 이상일 경우 break
        elif (scoville[0] >= k):
            break
        
        # k보다 적은 맵기가 있을경우 제시된 방법 진행 및 answer + 1
        else:
            scoville.append(scoville[0] + (scoville[1] * 2))
            for i in range(2):
                scoville.pop(0)
            
            answer += 1
            
    return answer
            
scoville = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(scoville, k))