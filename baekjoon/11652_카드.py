import sys
input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]
countNumber = dict()

for number in numbers:
	if number in countNumber:
		countNumber[number] += 1
	else:
		countNumber[number] = 0

maxNumber = max(countNumber.values())

num = [ key for key, value in countNumber.items() if maxNumber == value]
print(min(num))