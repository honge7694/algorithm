# 상근이가 갖고있는 숫자 카드.
N = int(input())
array1 = list(map(int, input().split()))
# 나열된 카드
M = int(input())
array2 = list(map(int, input().split()))

cnt = {}
for i in array1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

# 이진탐색을 위한 sort
array1.sort()

for i in array2:
    start, end = 0, N-1
    isExist = False

    while start <= end:
        mid = (start + end) //2

        if array1[mid] == i:
            print(cnt.get(i), end=' ')
            isExist = True
            break
        elif array1[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    
    if isExist == False:
        print(0, end=' ')




