import sys
input = sys.stdin.readline

N = int(input())
tmp = dict()

for _ in range(N):
	name, status = input().split()
	
	# 출근시 입력
	if status == "enter":
		tmp[name] = status
	# 퇴근시 삭제
	else:
		del tmp[name]

tmp = sorted(tmp.keys(), reverse=True)
print('\n'.join(tmp))




"""
peoples = [input().split() for _ in range(N)]
tmp = []

for people in peoples:
	if people[1] == "enter":
		tmp.append(people[0])
	else:
		tmp.remove(people[0])


print('\n'.join(tmp))
"""