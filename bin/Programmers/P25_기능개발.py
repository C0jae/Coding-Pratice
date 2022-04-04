def solution(progresses, speeds):
    answer = []
    
    # 각 프로그래스별 100%가 되기위한 시간을 표시하는 리스트 time 및 변수 cnt 선언
    time = []
    cnt = 0
    
    for i in range(len(progresses)):
        # progress가 100 이상이 될때까지의 시간 산출
        while(progresses[i] < 100):
            cnt += 1
            progresses[i] += speeds[i]
        
        time.append(cnt)
        cnt = 0
    
    # 동시에 배포되는 수를 나타내는 count 변수 선언
    count = 1
    
    for i in range(len(time) - 1):
        # 앞의 작업의 시간이 뒤 작업의 시간보다 오래걸린다면
        # 앞의 작업과 같이 배포를 해야하므로 count 1씩 증가 및 다음 작업의 시간과 비교
        if (time[i] >= time[i + 1]):
            time[i + 1] = time[i]
            count += 1
            continue
        
        # 다음 작업의 배포시간이 더 오래걸릴 경우 그 전 작업까지의 수가 같이 배포될 수가 된다.
        # 해당 배포 수(count)를 answer변수에 append
        # 다음 작업부터 남은 작업들의 배포수 산출을 위해 count = 1로 초기화
        answer.append(count)
        count = 1
    
    # 마지막 작업의 배포수 append
    answer.append(count)    
    
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))