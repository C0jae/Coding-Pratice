def solution(words, queries):
    answer = [0] * len(queries) # 답 추출하는 answer 리스트
    
    # queries와 words를 비교
    for i in range(len(queries)):
        for j in words:
            # 두 단어의 길이가 일치하지 않는다면 continue
            if len(queries[i]) != len(j):
                continue
            
            # queries가 모두 "?"로 이루어져 있을경우 조건 충족 => answer +1 후 다음 단어 확인
            if queries[i].count("?") == len(j):
                answer[i] += 1
                continue
            
            # 이진탐색을 위한 시작과 끝 인덱스 변수 선언
            start = 0
            end = len(queries[i]) - 1
            
            # "?"가 아닌 영어가 시작되는 or 끝나는 지점(인덱스) 찾기
            index = int(check(queries, i, start, end))
            
            # "?"가 앞부분에 있을경우 영어가 시작되는 지점 부터 두 단어가 일치할 경우 조건 충족 => answer +1
            if queries[i][0] == "?" and queries[i][index:] == j[index:]:
                answer[i] += 1
            # "?"가 뒷부분에 있을경우 첫 지점부터 영어가 끝나는 지점까지 두 단어가 일치할 경우 조건 충족 => answer +1
            elif queries[i][-1] == "?" and queries[i][:index + 1] == j[:index + 1]:
                answer[i] += 1
            
    return answer

# 이진탐색
def check(queries ,i, start, end):
    while start <= end:
        mid = (start + end) // 2    # 중간지점 mid 선언
        # 단어가 "?"로 시작하면서 뒷부분이 영어일 경우
        if queries[i][0] == "?":
            # 중간 지점이 영어단어 이면서 바로 앞 지점이 "?"일 경우 중간 지점의 인덱스 return
            if queries[i][mid] != "?" and queries[i][mid - 1] == "?":
                return mid
            # 중간 지점이 영어이지만 앞부분도 영어일 경우 => 시작부분부터 중간 지점까지 범위 재 설정 후 탐색
            elif queries[i][mid] != "?" and queries[i][mid - 1] != "?":
                end = mid
                check(queries ,i, start, end)
            # 중간 지점이 "?" 이면서 뒷부분도 "?"일 경우 => 중간 지점부터 끝 지점까지 범위 재 설정 후 탐색
            elif queries[i][mid] == "?" and queries[i][mid + 1] == "?":
                start = mid
                check(queries ,i, start, end)
            # 중간 지점이 "?" 이지만 바로 뒷 지점은 영어일 경우 중간 + 1 지점의 인덱스 return
            elif queries[i][mid] == "?" and queries[i][mid + 1] != "?":
                return mid + 1
        
        # 단어가 영어로 시작하면서 뒷부분이 "?"일 경우    
        else:
            # 중간 지점이 영엉이지만 바로 뒷 지점이 "?"일 경우 => 중간 지점의 인덱스 return
            if queries[i][mid] != "?" and queries[i][mid + 1] == "?":
                return mid
            # 중간 지점이 영어이면서 뒷 지점도 영어일 경우 => 중간 지점부터 끝 지점까지 범위 재 설정 후 탐색
            elif queries[i][mid] != "?" and queries[i][mid + 1] != "?":
                start = mid
                check(queries ,i, start, end)
            # 중간 지점이 "?" 이면서 앞 지점도 "?" 일 경우 => 시작 지점부터 중간 지점까지 범위 재 설정 후 탐색
            elif queries[i][mid] == "?" and queries[i][mid - 1] == "?":
                end = mid
                check(queries ,i, start, end)
            # 중간 지점이 "?" 이지만 바로 앞 지점은 영어일 경우 => 중간 -1 지점의 인덱스 리턴
            elif queries[i][mid] == "?" and queries[i][mid - 1] != "?":
                return mid - 1
        
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))