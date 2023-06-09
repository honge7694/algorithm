"""
92p
1. N, M, K를 입력을 받는다.
2. M번만큼 숫자를 더한다.
3. 조건 : K 만큼 가장 큰 수를 반복하여 더할 수 있다.
4. K만큼 더했으면 다음으로 큰 수를 더하여 가장 큰 수를 만든다.
5. 4.를 만족하면 다시 3.을 반복한다.

"""
import sys

N, M, K = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))
count = 0
result = 0

number_list.sort()
for i in range(M):
    if count < K:
        result += number_list[-1]
        count += 1
        print(f"{i}번째, {result}")
        continue
    count = 0
    result += number_list[-2]
    print(f"{i}번째, {result}")
    
print(result)
