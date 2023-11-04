N = int(input())

dataList = []
for _ in range(N):
    dataList.append(input())

for data in dataList:
    stack = []
    for char in data:
        # 1. 열린 괄호는 스택으로
        if char == "(":
            stack.append(char)
        elif char == ")":
            # 3. 잘못된 VPS
            if not stack:
                stack.append(char)
                break
            # 2. 옳바른 VPS
            pair = stack.pop()
            if char==')' and pair=='(':
                continue
    
    if not stack:
        print("YES")
    else:
        print("NO")