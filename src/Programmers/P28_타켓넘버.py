# 전역변수 answer 선언
answer = 0

def solution(numbers, target):
    global answer
    
    # dfs함수 이용(0번째, 합, numbers, target)
    dfs(0, 0, numbers, target)
    return answer


# dfs 함수 선언
def dfs(a, s, numbers, target):
    global answer
    n = len(numbers)
    
    # n번째 계산까지 완료되었을 경우의 합이 target과 같으면 answer + 1
    if a == n:
        if s == target:
            answer += 1
            return
    
    # 아직 n번째에 도달하지 못하였다면 a번째의 값을 더하거나 뺀 후 a + 1번째 기준 함수 적용
    else:
        dfs(a + 1, s + numbers[a],numbers, target)
        dfs(a + 1, s - numbers[a],numbers, target)


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))



def solution2(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])