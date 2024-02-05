import sys
input = sys.stdin.readline

N = int(input())

text = [input().strip() for _ in range(N)]
text = list(set(text)) # 중복 제거
text.sort() # 사전순 정렬
text.sort(key=len) # 길이 정렬

print('\n'.join([txt for txt in text]))

# 정렬 비싼 연산. 2번 사용 X
# unsolved
