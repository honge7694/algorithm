N = int(input())

temp = True
result = []
stack = []
count = 1

for i in range(N):
    num = int(input())

    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        temp = False
        break

if temp :
    for i in result:
        print(i)
else:
    print("NO")





