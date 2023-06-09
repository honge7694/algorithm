"""
96p
"""
import sys

N, M = map(int, sys.stdin.readline().split())

result = 0
for _ in range(N):
    card = list(map(int, sys.stdin.readline().split()))

    min_number = min(card)
    result = max(result, min_number)

print(result)