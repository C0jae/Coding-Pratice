from abc import abstractmethod


def solution(s):
    # s의 길이를 나타낸는 cnt 변수 선언
    cnt = int(len(s))
    
    # 문자열 길이가 홀수일경우 가운데 문자 리턴
    if (cnt % 2 != 0):
        return s[cnt//2]
    # 문자열 길이가 홀수일 경우 가운데 두개의 문자 리턴
    else:
        cnt = int(cnt / 2)
        return s[cnt-1 : cnt+1]

def solution2(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]

s = "abcd"

print(solution(s))
print(solution2(s))
