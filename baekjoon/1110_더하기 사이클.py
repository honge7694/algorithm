N = int(input())
count = 0
number = N # N과 같아질 때까지 변할 수
result = 0 # 더한 값의 결과
while True:
    a = number // 10 # 10의 자리
    b = number % 10 # 1의 자리
    result = a + b
    number = int(str(b) + str(result)[-1])
    count += 1

    if N == number:
        break
    # if count == 0:
    #     result = int(str(N)[0]) + int(str(N)[-1])
    #     number = int(str(N)[1] + str(result)[-1])
    #     count += 1
    # else:
    #     result = int(str(number)[0])+ int(str(number)[-1])
    #     number = int(str(number)[-1] + str(result)[-1])
    #     count += 1

print(count)