def isValid(s: str) -> bool:
    stack = []
    
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in "]})":
            if not stack:
                return False
            top = stack.pop()

            if top == '(' and char == ')':
                continue
            elif top == '{' and char == '}':
                continue
            elif top == '[' and char == ']':
                continue
            else:
                return False
        
    return not stack

s = "()"
s2 = "()[]{}"
s3 = "(]"
print(isValid(s3))