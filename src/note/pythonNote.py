m = int(input("버스 수 : "))    # 버스 개수 입력

bus = []
for _ in range(m):
    bus.append(list(map(int, input("버스 정보 입력 : ").split())))
    
print(len(bus[0]))