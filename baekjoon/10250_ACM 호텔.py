'''
T = 테스트 데이터
H = 높이
W = 가로
N = N 번째 손님

방법 1.
손님을 room[0][0], room[1][0], room[2][0]... 으로 안내한다.
'''

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    rooms = [[0] * W for _ in range(H)]
    count = 0

    for i in range(W):
        for j in range(H):
            # rooms[j][i] = str(j+1) + '0' + str(i+1)
            rooms[j][i] = (j+1) * 100 + i+1
            count += 1
            if count == N:
                print(int(rooms[j][i]))
                break