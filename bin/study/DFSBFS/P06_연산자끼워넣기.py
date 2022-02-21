def solution(i, result):
    global add, sub, mul, div, max_value, min_value
    
    # 모든 수의 연산이 끝났을 경우 최대값 및 최소값 설정
    if i == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    
    else:
        # 연산의 수가 남아있을경우
        if add > 0:
            add -= 1
            # 해당연산의 수를 -1 한 후에 재귀함수 적용
            solution(i + 1, result + number[i])
            
            # 다른 경우의 수의 판별을 위해 감소시킨 연상 원상복귀
            add += 1
        
        if sub > 0:
            sub -= 1
            solution(i + 1, result - number[i])
            sub += 1
        
        if mul > 0:
            mul -= 1
            solution(i + 1, result * number[i])
            mul += 1
            
        if div > 0:
            div -= 1
            solution(i + 1, int(result / number[i]))
            div += 1

n = int(input("수의 갯수 : "))
number = list(map(int, input("수 : ").split()))
add, sub, mul, div = map(int, input("연산자 갯수 : ").split())

max_value = -1e9
min_value = 1e9

solution(1, number[0])

print(max_value)
print(min_value)