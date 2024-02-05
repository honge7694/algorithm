import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

resultA = len(set(A) - set(B))
resultB = len(set(B) - set(A))


print(resultA + resultB)

"""
입력받은 수 (A + B) - A와 B 중복 된 수
"""
