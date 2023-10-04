def binary_search(array, target, start, end):
    if start >= end:
        return 0

    mid = (start + end) // 2
    
    if array[mid] == target:
        return card_count.get(target)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start,mid-1)


N = int(input())
player = sorted(list(map(int, input().split())))
M = int(input())
number_cards = list(map(int, input().split()))

card_count = {}
for i in player:
    if i in card_count:
        card_count[i] += 1
    else:
        card_count[i] = 1

for card in number_cards:
    print(binary_search(player, card, 0, len(player)-1), end=' ')


