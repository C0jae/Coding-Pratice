def solution(s):
    result = []
    
    # 문자열의 길이가 1이라면 1을 리턴
    if len(s) == 1:
        return 1
    
    # 문자열 s의 중간까지 반복문 실행
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1
        
        # i - 1번째 까지 하나의 묶음으로 설정
        tmp = s[:i]
        
        # i번째부터 i단위로 반복문 실행
        for j in range(i, len(s), i):
            
            # tmp묶음과 다음 묶음의 문자열이 같을경우 cnt + 1
            if tmp == s[j:i+j]:
                cnt += 1
            
            else:
                # 묶음 횟수가 1이상이면 앞에 숫자 표시
                if cnt != 1:
                    b = b + str(cnt) + tmp
                
                # 묶음 횟수가 1이라면 숫자표시 x
                else:
                    b = b + tmp
                
                # 최근 그룹의 문자열로 최신화
                tmp = s[j:j + i]
                cnt = 1
        
        if cnt != 1:
            b = b + str(cnt) + tmp
        
        else:
            b = b + tmp
        
        result.append(len(b))
    
    return min(result)