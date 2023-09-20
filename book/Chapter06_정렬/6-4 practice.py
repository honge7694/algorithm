array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # array[pivot]보다 큰 값을 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # array[pivot] 보다 작은 값을 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right: # left와 right가 엇갈렸다면 작은 값과 pivot을 교체하여 분할
            array[pivot], array[right] = array[right], array[pivot]
        else: # 그게 아니라면 작은 값과 큰 값을 교체
            array[left], array[right] = array[right], array[left]
        
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)