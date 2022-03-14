def solution(words, queries):
    answer = [0] * len(queries)
    
    for i in range(len(queries)):
        for j in words:
            if len(queries[i]) != len(j):
                continue
            
            if queries[i].count("?") == len(j):
                answer[i] += 1
                continue
            
            start = 0
            end = len(queries[i]) - 1
            
            index = int(check(queries, i, start, end))
            
            if queries[i][0] == "?" and queries[i][index:] == j[index:]:
                answer[i] += 1
            elif queries[i][-1] == "?" and queries[i][:index + 1] == j[:index + 1]:
                answer[i] += 1
            
    return answer


def check(queries ,i, start, end):
    while start <= end:
        mid = (start + end) // 2
        if queries[i][0] == "?":
            if queries[i][mid] != "?" and queries[i][mid - 1] == "?":
                return mid
            elif queries[i][mid] != "?" and queries[i][mid - 1] != "?":
                end = mid
                check(queries ,i, start, end)
            elif queries[i][mid] == "?" and queries[i][mid + 1] == "?":
                start = mid
                check(queries ,i, start, end)
            elif queries[i][mid] == "?" and queries[i][mid + 1] != "?":
                return mid + 1
            
        else:
            if queries[i][mid] != "?" and queries[i][mid + 1] == "?":
                return mid
            elif queries[i][mid] != "?" and queries[i][mid + 1] != "?":
                end = mid
                check(queries ,i, start, end)
            elif queries[i][mid] == "?" and queries[i][mid - 1] == "?":
                start = mid
                check(queries ,i, start, end)
            elif queries[i][mid] == "?" and queries[i][mid - 1] != "?":
                return mid - 1
        
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))