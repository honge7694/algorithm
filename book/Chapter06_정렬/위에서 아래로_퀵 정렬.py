N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

def quick_sort(array, start, end):
    if start >= end:
        return 

    pivot = start
    left = start+1
    right = end

    while left <= right:
        # array[pivot]보다 left 값이 작은 값을 찾을 때까지
        while left <= end and array[pivot] <= array[left]:
            left += 1
        
        # array[pivot]보다 right 값이 큰 값을 찾을 때까지
        while right >= start and array[pivot] >= array[right]:
            right -= 1
        
        # left와 right가 엇갈렸다면 pivot 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 엇갈리지 않았다면 left, right 교체
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)

for data in array:
    print(data, end=' ')