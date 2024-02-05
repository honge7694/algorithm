import sys
input = sys.stdin.readline

def combin(num):
	result = 1
	for i in range(1, num+1):
		result *= i
	return result


count = int(input())

for case in range(count):
	n, m = map(int, input().split())
	
	result = combin(m) // (combin(m-n) * combin(n))
	print(result)