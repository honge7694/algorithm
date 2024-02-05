import sys
input = sys.stdin.readline

N = int(input())
count = 0
users = set()

for _ in range(N):
	user = input().strip()
	# ENTER 일 때, 모든 유저 POP
	if user == "ENTER":
		users.clear()
	# ENTER 후, 처음 채팅을 등록 USER 
	else:
		if not user in users:
			count += 1
			users.add(user)
			
print(count)