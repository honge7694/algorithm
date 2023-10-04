import sys
input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]

# 산술평균
result = round(sum(array) / len(array))
print(int(result))

# 중앙값
mid = len(array) // 2
result = sorted(array)
print(result[mid])

# 최빈값
number = {}
for i in array:
    if i in number:
        number[i] += 1
    else:
        number[i] = 1

max_number = max(number.values())

result = []
for key, value in number.items():
    if value == max_number:
        result.append(key)

result.sort()
if len(result) > 1:
    print(result[1])
else:
    print(result[0])



# 범위
print(max(array) - min(array))
