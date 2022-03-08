def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    filter_report = list(set(report))
    split_report = []
    
    for i in filter_report:
        split_report.append(i.split(" "))
    
    print(split_report)
    
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))