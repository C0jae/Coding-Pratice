def solution(dartResult):
    # 다트 3개의 점수 표시
    score = []
    # 최근에 던진 다트의 점수
    n = ''
    
    for i in dartResult:
        # 문자열이 숫자(점수)일 경우 n에 할당
        if (i.isnumeric()):
            n += i
        
        # S일 경우 n에 1제곱 후 해당 점수 score에 할당
        # 점수 계산이 끝났으므로 다음 다트를 위해 n 초기화
        elif (i == 'S'):
            n = int(n) ** 1
            score.append(n)
            n = ''
        
        elif (i == 'D'):
            n = int(n) ** 2
            score.append(n)
            n = ''
            
        elif (i == 'T'):
            n = int(n) ** 3
            score.append(n)
            n = ''
        
        # *일 경우 전에 던진 다트가 있을경우 이전점수화 현재점수 각각 x2
        # 전에 던진 다트가 없을경우 현재 다트점수만 x2
        elif (i == '*'):
            if (len(score) > 1):
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            
            else:
                score[-1] = score[-1] * 2
        
        # #일 경우 현재 점수에 x -1
        elif (i == '#'):
            score[-1] = score[-1] * -1
    
    return sum(score)


# dartResult = list(input("다트 결과 : "))
dartResult = "1S2D*3T"

print(solution(dartResult))