N, M = map(int, input().split())

array1 = set()
for i in range(N):
    array1.add(input())

array2 = set()
for i in range(M):
    array2.add(input())

result = sorted(list(array1 & array2))
print(len(result))
for i in result:
    print(i)
