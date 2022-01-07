import heapq

def solution(scoville, k):
    answer = 0
    
    while True:
        if (len(scoville) == 1 and scoville[0] < k):
            answer = -1
            break;
            
        elif (scoville[0] >= k):
            break
        
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            
            heapq.heappush(scoville, a + (b * 2))
            answer += 1
    
    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(scoville, k))
