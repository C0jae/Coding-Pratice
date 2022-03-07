def check(answer):
    for x, y, a in answer:
        # 기둥일 경우
        if a == 0:
            # 기둥의 구조적 조건을 만족할 경우
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            
            # 기둥의 구조적 조건이 만족하지 않을경우
            return False
        
        # 보일 경우
        elif a == 1:
            # 보의 구조적 조건을 만족할 경우
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            
            return False
        
    return True


def solution(n, build_frame):
    answer = []
    
    # x, y 좌표, 구조물 종류, 설치 및 제거 여부에 대한 변수지정
    for frame in build_frame:
        x, y, a, b = frame
        
        # 제거 대상일 경우 제거를 한 후 구조물의 조건 충족여부 확인
        if b == 0:
            answer.remove([x, y, a])
            # 조건을 충족하지 않을경우 다시 해당 구조물 추가
            if not check(answer):
                answer.append([x, y, a])
        
        # 설치 대상일 경우 설치후 구조물의 조건 충족여부 확인
        if b == 1:
            answer.append([x, y, a])
            # 조건을 충족하지 않을경우 다시 해당 구조물 제거
            if not check(answer):
                answer.remove([x, y, a])
    
    # 정렬 후 출력
    return sorted(answer)