import itertools


def solution(word):
    dic = ['A', 'E', 'I', 'O', 'U']
    data = []
    
    # 1개 ~ 6개의 모든 조합 하나의 리스트에 넣기
    for i in range(1, 6):
        data.extend(list(map(''.join, itertools.product(dic, repeat = i))))
    
    # 정렬
    data.sort()
    
    # 해당 위치 출력(인덱스 + 1)
    return data.index(word) + 1

word = "AAAAE"
print(solution(word))