N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

for data in array:
    print(data, end=' ')

