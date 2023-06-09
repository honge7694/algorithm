import sys

N = int(input())

num_list = [int(sys.stdin.readline()) for _ in range(N)]
    
set(num_list)
num_list.sort()
[print(i) for i in num_list]
    
    