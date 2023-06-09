"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 
동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

1. 가장 큰 순서로 대입하여 나눈다.
"""
import sys

N, K = map(int, sys.stdin.readline().split())
coin_list = []
coin_count = 0

for _ in range(N):
    coin_list.append(int(sys.stdin.readline()))
coin_list.sort(reverse=True)

for coin in coin_list:
    if K // coin > 0:
        coin_count += K // coin
        K %= coin

sys.stdout.write(str(coin_count))
