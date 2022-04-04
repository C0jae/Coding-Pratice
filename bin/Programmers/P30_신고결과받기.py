# 시간초과 1

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
    
#     report_filter = []
#     report_split = []
#     target = []
    
#     report_filter = list(set(report))
    
#     # 신고자와 신고당한자를 배열로 분리 및 중복 신고 삭제
#     for i in report_filter:
#         report_split.append(i.split(" "))
    
#     # 정지될 유저 선별
#     for i in id_list:
#         cnt = 0
#         for j in range(len(report_split)):
#             if i == report_split[j][1]:
#                 cnt += 1
                
#                 if cnt == k:
#                     target.append(i)
    
#     for i in range(len(id_list)):
#         for j in target:
#             for z in range(len(report_split)):
#                 if id_list[i] == report_split[z][0] and j == report_split[z][1]:
#                     answer[i] += 1
    
#     return answer




# 시간초과 2

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    filter_report = list(set(report))   # 신고내역 중복제거
    split_report = []   # 신고내역의 피해자 피의자 리스트 구분
    victim = []         # 신고내역의 피해자 리스트
    suspect = []        # 신고내역의 피의자 리스트
    target = []         # 정지대상
    index = []
    
    # 피해자 및 피의자 구분
    for i in range(len(filter_report)):
        split_report.append(filter_report[i].split(" "))
        victim.append(split_report[i][0])
        suspect.append(split_report[i][1])
    
    # 정지대상 유저 식별
    for i in range(len(suspect)):
        if suspect.count(suspect[i]) >= k:
            index.append(i)
            
            if suspect[i] not in target:
                target.append(i)
                
    for i in range(len(id_list)):
        for j in index:
            if id_list[i] == victim[j]:
                answer[i] += 1
    
    return answer




def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    return answer
    

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))