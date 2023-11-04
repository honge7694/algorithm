import sys
input = sys.stdin.readline

N = int(input().strip())
nums = [int(input()) for _ in range(N)]

result = []
stack = []
count = 1
temp = True

for num in nums:
    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1
    
    if num == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        temp = False

if temp:
    for i in result:
        print(i)
else:
    print("NO")
