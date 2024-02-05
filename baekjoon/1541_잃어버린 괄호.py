import sys, re
input = sys.stdin.readline


N = input().split("-") # -를 기준으로 나눈다
sum_result = [] # +가 있는 항들의 합을 넣는다

for i in N:
	# sum_result.append(eval(i)) # string 연산을 처리해준다. (0시작 에러)
	tmp = 0
	arr = i.split('+')
	for j in arr:
		tmp += int(j) # +가 있는 항들 연산
	sum_result.append(tmp)

answer = sum_result[0]
for i in range(1, len(sum_result)): # 첫번째 값에서 나머지 값 빼기
	answer -= sum_result[i] 

print(answer)


