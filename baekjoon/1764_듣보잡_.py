import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

# set은 정렬 x, list로 변환
result = set(A) & set(B) # set은 교집합 처리 가능
result = sorted(result)

# 결과 출력
print(len(result))
for text in result:
	print(text, end='')