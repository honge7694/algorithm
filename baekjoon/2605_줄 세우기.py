import sys

# 1. 처음에 큐를 이용해야겠다 했는데, queue를 이용해 어떻게 접근?
# 2. list를 한개 더 추가로 변경
# 3. 일단 들어오는 값 모두 받아보기
# 4. 0 0 0 1 0을 하니까 5, 3, 4, 2, 1이 되는 것을 확인
# 5. reverse 하면 된다

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
result = []

for i in range(len(numbers)):
	# 0은 제자리에 들어가기 때문에 index 0에 insert
	if numbers[i] == 0:
		result.insert(0, i+1)
	# 나머지는 numbers[i]의 값에 insert
	else :
		result.insert(numbers[i], i+1)

reverse_result = result[::-1]

print(' '.join(map(str, reverse_result)))
