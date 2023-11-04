# M 이상 N 이하의 소수 모두 구하기


def sosu(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
    


N, M = map(int, input().split())
answer = []
for i in range(N, M+1):
    if sosu(i):
        answer.append(i)

for i in answer:
    print(i)