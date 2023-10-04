N = int(input())

result = []
for i in str(N):
    result.append(i)

result.sort(reverse=True)
result = int(''.join(result))

if result % 3 != 0 or result % 30 != 0:
    print(-1)
else:
    print(result)