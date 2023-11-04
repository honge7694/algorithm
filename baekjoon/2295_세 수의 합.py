N = int(input())

array = []
for i in range(N):
    array.append(int(input()))


count = 0
sum_arr = 0
result = 0
for i in range(len(array)-1, -1, -1):
    for j in range(i-1, -1, -1):
        if count == 3:
            continue
        sum_arr += array[j]
        count += 1
    if count == 3 and array[i] == sum_arr:
        print(array[i])
    

