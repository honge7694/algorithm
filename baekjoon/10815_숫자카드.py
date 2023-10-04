def binary_search(array, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

N = int(input())
player = sorted(list(map(int, input().split())))

M = int(input())
cards = list(map(int, input().split()))

for card in cards:
    print(binary_search(player, card, 0, len(player)-1), end=' ')


