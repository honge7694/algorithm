N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            break
        else :
            array[j-1], array[j] = array[j], array[j-1]

for data in array:
    print(data, end=' ')

    