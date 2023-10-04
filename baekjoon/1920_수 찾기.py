import sys

N = int(sys.stdin.readline().rstrip())
array1 = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
array2 = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진탐색을 위한 sort
array1.sort()

for i in array2:
    start, end = 0, N-1
    isExist = False

    # 반복문을 이용한 이진탐색
    while start <= end:
        mid = (start + end) // 2

        if array1[mid] == i:
            isExist = True
            print(1)
            break
        # array1[mid] 값보다 i가 더 큰 경우
        elif i > array1[mid]:
            start = mid + 1
        # array1[mid] 값보다 i가 더 작은 경우
        else:
            end = mid - 1
    
    if isExist == False:
        print(0)