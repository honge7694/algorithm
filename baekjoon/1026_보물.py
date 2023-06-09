"""
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 
김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
길이가 N인 정수 배열 A와 B가 있다. 
다음과 같이 함수 S를 정의하자.

S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자.
단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.

1. A배열 작은 값을 B의 큰 값과 인덱스가 같게한다.
2. B의 가장 큰 값 인덱스를 구하고 A의 최소 인덱스를 넣는다.

"""
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
S = 0

for _ in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

sys.stdout.write(str(S))
