import collections
N = int(input())

list1 = []
for i in range(N):
    list1.append(i+1)

dirty_dish = collections.deque(list1)
wash_dish = collections.deque()
dry_dish = collections.deque()

while True:
    if not dirty_dish and not wash_dish:
        break

    a, b = map(int, input().split())

    if a == 1:
        for _ in range(b):
            wash_dish.append(dirty_dish.popleft())

    elif a == 2:
        for _ in range(b):
            dry_dish.append(wash_dish.pop())

while len(dry_dish) != 0:
    print(dry_dish.pop())


