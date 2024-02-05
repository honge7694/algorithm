import itertools
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
cards = [int(input()) for _ in range(N)]
print(len(set("".join(str(i)) for i in itertools.permutations(cards, K))))

## 재귀함수로 풀어보기.