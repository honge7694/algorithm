def sieve_of_eratosthenes(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1) :
        if number % i == 0 :
            return False
    return True

result = 0

while True:
    result = 0
    N = int(input())
    if N == 0:
        break
    N2 = N * 2

    for i in range(N, (N2+1)):
        if sieve_of_eratosthenes(i):
            result += 1
    print(result)

