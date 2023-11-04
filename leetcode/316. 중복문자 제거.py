def removeDuplicateLetters(s: str) -> str:
    stack = []

    # 1. 딕셔너리를 이용하여 단어 카운트
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    # 2. 카운트가 1인 값은 스택에 쌓기
    for char in s:
        if count[char] == 1:
            stack.append(char)
        else:
            count[char] -= 1
            continue
    
    return "".join(stack)



s = "bcabc"
s1 = "cbacdcbc"
print(removeDuplicateLetters(s1))
