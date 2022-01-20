def solution(s):
    data = []
    
    for i in s:
        # data에 들어있는 숫자가 없을 때
        if len(data) == 0:
            data.append(i)
        
        # 가장 오른쪽에 있는 수와 i가 같을경우 data에서 해당 숫자 제거
        elif data[-1] == i:
            data.pop()
        
        # 가장 오른쪽 수와 i가 다를경우 data에 i를 추가
        else:
            data.append(i)
    
    if len(data) == 0:
        return 1
    
    else:
        return 0
            
print(solution("baabaa"))