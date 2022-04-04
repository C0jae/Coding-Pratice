def solution(n):
    answer = ''
    
    # (n - 1) % 3 = 0, 1, 2 일때 1, 2, 4 이므로 '124'의 리스트 형식으로 활용 가능
    while (n > 0):
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3
        
    return answer
    
n = 10

print(solution(n))