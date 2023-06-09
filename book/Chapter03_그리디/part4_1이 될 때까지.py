"""
1. N이 -1하여 1이 되거나, 나누어 몫이 1이 되게하기.
2. 위 과정을 제일 빠르게 하는 것을 찾는다.
"""

import sys

N, K = map(int, sys.stdin.readline().split())
result = N
count = 0

while(True):
    if result == 1:
        break
    elif result % K == 0 :
        result //= K
        count += 1
    else:
        result -= 1
        count += 1

print(count)



