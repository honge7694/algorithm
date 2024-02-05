import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
	text = input().split()
	reverse_text = text[::-1]
	
	print(f"Case #{i+1}:", ' '.join(map(str, reverse_text)))
