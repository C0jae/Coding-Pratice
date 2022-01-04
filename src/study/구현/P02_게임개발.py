# def check(x, y):

# 방문한 칸의 수    
cnt = 0

# 방향을 돌린 횟수
time = 0

n, m = map(int, input("행, 열 입력 : ").split())
a, b, d = map(int, input("캐릭터 위치 및 방향 표시 : ").split())

# 나침반(북, 동, 남, 서)
cd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

data = [[0] * m for i in range(n)]

for i in range(n):
    data[i] = list(map(int,input("행 바다 or 육지 선택 : ").split()))
        
while True:
    # 움직이려는 방향이 d 범위안에 있을경우
    if (a + cd[d][0] >= 0 and a + cd[d][0] < n and
        b + cd[d][1] >= 0 and b + cd[d][1] < m):
        
        print("======================")
        print("카운트 : ", cnt)
        print("time : ", time)
        print("방향 : ", d)
        print("땅 : " ,data[a + cd[d][0]][b + cd[d][1]])
        
        # 움직이려는 방향이 육지인경우
        if (data[a + cd[d][0]][b + cd[d][1]] == 0):
            time = 0
            print("이동 좌표1 : ", a, b)
            
            # 이동을 시작한 지점은 0 -> 2로 표시
            data[a][b] = 2
            a += cd[d][0]
            b += cd[d][1]
            print("이동 좌표2 : ", a, b)
            cnt += 1
            
        # 움직이려는 방향이 바다인경우
        else:
            # 방향전환
            if (d == 0): d = 3
            elif (d == 1): d = 0
            elif (d == 2): d = 1
            elif (d == 3): d = 2
            time += 1
            
            # 4방향 모두 가본칸이거나 바다일 경우 + 뒤로 이동 가능할 경우
            if (time == 6 and data[a + cd[d][0]][b + cd[d][1]] == 2):
                # 뒤로 이동을 시작한 지점은 3으로 표시
                data[a][b] = 3
                a += cd[d][0]
                b += cd[d][1]
                cnt += 1
                time = 0
                print("=======뒤로이동=======")
                print("이동좌표 : ", a, b)
                print("======================")
                
                continue
            
            # 4방향 모두 기본칸이거나 바다일 경우 + 뒤로 이동 불가능할 경우 종료
            # 뒤로 한칸 이동을 보는방향의 반대방향까지 돌아서 앞으로 이동하는거로 대체(time = 6을 조건으로 건 이유)
            elif (time == 6 and data[a + cd[d][0]][b + cd[d][1]] != 2):
                break
        
            continue
            
    else:
        # 방향전환
            if (d == 0): d = 3
            elif (d == 1): d = 2
            elif (d == 2): d = 1
            elif (d == 3): d = 0
            time += 1
            
            print("방향 막힘", cnt)
            
            if (time == 6):
                break
            
            
        
print(cnt)