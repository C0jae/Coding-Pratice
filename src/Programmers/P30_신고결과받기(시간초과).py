def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report_filter = []
    report_split = []
    target = []
    
    report_filter = list(set(report))
    
    # 신고자와 신고당한자를 배열로 분리 및 중복 신고 삭제
    for i in report_filter:
        report_split.append(i.split(" "))
    
    # 정지될 유저 선별
    for i in id_list:
        cnt = 0
        for j in range(len(report_split)):
            if i == report_split[j][1]:
                cnt += 1
                
                if cnt == k:
                    target.append(i)
    
    for i in range(len(id_list)):
        for j in target:
            for z in range(len(report_split)):
                if id_list[i] == report_split[z][0] and j == report_split[z][1]:
                    answer[i] += 1
    
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))