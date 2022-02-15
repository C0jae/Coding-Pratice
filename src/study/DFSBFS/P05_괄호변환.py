# 균형있는 코드여부 검토 -> 균형있지 않았다면 균형있던 곳 까지의 인덱스 리턴
def balaced_index(p):
    count = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        
        else:
            count -= 1
        
        if count == 0:
            return i

# 올바른 문자여부 검토
def check_proper(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        
        else:
            # 남아있는 '('가 없이 ')'가 올 경우 올바른 문자x
            if count == 0:
                return False
            
            count -= 1
    
    # 올바른 문자로 판별되면 True 리턴
    return True


def solution(p):
    answer =''
    
    # 아무런 단어도 없다면 빈 answer 리턴
    if p == '':
        return answer
    
    # 균형있는 곳까지의 인덱스 값 가져오기
    index = balaced_index(p)
    # 균형있는 곳까지의 값 u
    u = p[:index + 1]
    
    # 균형있지 않은 곳부터의 값 v
    v = p[index + 1:]
    
    # 균형있는 u값이 제대로 배열도 되어있을경우 answer에 u값 적용 및 v값만으로 다시 반복
    if check_proper(u):
        answer = u + solution(v)
    
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        u = list(u[1:-1])
        
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            
            else:
                u[i] = '('
            
        answer += "".join(u)
        
    return answer

p = "()))((()"

print(solution(p))