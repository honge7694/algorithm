import sys
input = sys.stdin.readline

N, M = map(int, input().split())
setText = [input() for _ in range(N)]
text = [input() for _ in range(M)] 
# warning 
# 입력받으면서 바로 체크 가능하면 시간 단축 가능
# set으로 바꿔서 진행하면 시간 단축 가능
count = 0

for txt in text:
	if txt in setText:
		count += 1

print(count)










# 이건 왜 안될까..
# print((N + M) - len(set(setText + text)))


