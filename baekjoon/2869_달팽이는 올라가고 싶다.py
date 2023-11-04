'''
A = 올라가는 높이
B = 내려가는 높이
V = 나무 높이

올라가야할 거리 = V - B
하루에 갈 수 있는 거리 = A - B

'''

A, B, V = map(int, input().split())
result = (V-B) / (A-B)

print(int(result) if int(result) == result else int(result) + 1)
